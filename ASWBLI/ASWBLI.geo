scale = 0.01;

r  = 10.15 * scale;  // Radius of shaft
R  = 50.00 * scale;  // Radius of domain
L  =  78.39 * scale;  // Length of section before flare
S  = 20.00 * scale;  // Length of flare
Dx =  5.00 * scale;  // Section after flare

theta = 20;

x1 = S * Cos(theta * Pi/180);
y1 = S * Sin(theta * Pi/180) + r;
dx1 = (R - y1) * Tan(theta * Pi/180);
dx2 = (R - r) * Tan(theta/2 * Pi/180);

Point(1) = {    -L,  r,  0, 1.0};
Point(2) = {     0,  r,  0, 1.0};
Point(3) = {    x1, y1,  0, 1.0};
Point(4) = {    -L,  R,  0, 1.0};
Point(5) = {  -dx2,  R,  0, 1.0};
Point(6) = {x1-dx1,  R,  0, 1.0};

Line(1) = {1, 2};  Line(2) = {2, 3};  Line(3) = {4, 5};
Line(4) = {5, 6};  Line(5) = {3, 6};  Line(6) = {2, 5};
Line(7) = {1, 4};

Curve Loop(1) = {3, -6, -1,  7};  Surface(1) = {1};
Curve Loop(2) = {6,  4, -5, -2};  Surface(2) = {2};

ratio     = 1.1;  // Expansion ratio in boundary layer
h0        = 1e-4;  // Height of first cell in boundary layer
thickness = 0.02;  // Thickness of boundary layer

// Aproximate number of cells in outer layer to match boundary layer
N1 = Floor(ratio * (R-r-thickness)/(thickness * (ratio - 1) + h0));

Transfinite Surface {1}; Transfinite Surface {2};

Transfinite Curve {7, 6, 5} = 50 Using Progression 1.05;
Transfinite Curve {3, 1} = 200 Using Bump 0.005;
Transfinite Curve {4, 2} = 60 Using Progression 1.1;

Field[1] = BoundaryLayer;
Field[1].Quads = 1;
Field[1].Thickness = 0.02;
Field[1].EdgesList = {1, 2};
Field[1].NbLayers = 20;
Field[1].NodesList = {1, 2, 3};
Field[1].Ratio = ratio;
Field[1].hwall_n = h0;
Field[1].hfar = 0.01;
Field[1].IntersectMetrics = 1;

BoundaryLayer Field = 1;

Recombine Surface {1, 2, 3};
Extrude {0, 0, 10*scale} {
  Surface{1,2};
  Layers{1}; Recombine;
}

Physical Surface("inlet", 77) = {28};
Physical Surface("wall", 78) = {24, 50};
Physical Surface("freestream", 79) = {16, 42};
Physical Surface("outlet", 80) = {46};
Physical Surface("wedge0", 81) = {2, 1};
Physical Surface("wedge1", 82) = {51, 29};

Physical Volume(1000) = {1, 2};
