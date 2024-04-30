scale = 0.001;

// Mesh size parameters

pSize  = 0.002;    // Size of triangular elements
pSize2 = 0.00025;  // Smaller size at location of lower shock
Delta0 = 1e-6;     // Height of first cell in boundary layer

//             pSize    pSize2   Delta0  y+ (approx.)
// veryCoarse  0.004    0.001    1e-3    50
// coarse      0.002    0.0005   1e-4     5
// medium      0.001    0.00025  1e-5     0.5
// fine        0.001    0.00025  1e-6     0.05

// Geometric Parameters

L1 = 500 * scale;  // Length of horizontal plate
L2 = 300 * scale;  // Length of angled plate
L3 = 550 * scale;  // Extension into freestream
L4 =  50 * scale;  // Length of inlet before plate

beta  = 10;    // Deflection angle in degrees
theta = 19.4;  // Corresponding wave angle at Mach 5

h  = 115 * scale;  // Height of inlet - given as y_gen in paper

x1 = 350 * scale;  // Location of impinging inviscid shock

x2 = x1 -  h / Tan(theta*Pi/180);
x3 = x2 + L2 * Cos(beta *Pi/180);
y2 =  h - L2 * Sin(beta *Pi/180);

// Mesh construction

Point(1) = {  0,  0, 0, pSize};
Point(2) = { x1,  0, 0, pSize2};
Point(3) = { L1,  0, 0, pSize};
Point(4) = { L3,  0, 0, pSize};
Point(5) = {-L4,  h, 0, pSize};
Point(6) = { x2,  h, 0, pSize};
Point(7) = { x3, y2, 0, pSize};
Point(8) = { L3, y2, 0, pSize};
Point(9) = {-L4,  0, 0, pSize};

Line(1) = {9, 1};  Line(2) = {1, 2};  Line(3) = {2, 3};
Line(4) = {3, 4};  Line(5) = {4, 8};  Line(6) = {8, 7};
Line(7) = {7, 6};  Line(8) = {6, 5};  Line(9) = {5, 9};

Curve Loop(1) = {7, 8, 9, 1, 2, 3, 4, 5, 6};
Plane Surface(1) = {1};

Field[1] = BoundaryLayer;
Field[1].Quads = 1;
Field[1].Thickness = 0.01;
Field[1].EdgesList = {6, 8, 7, 4, 3, 2, 1};
Field[1].NbLayers = 10;
Field[1].NodesList = {9, 5, 8, 4};
Field[1].Ratio = 1.15;
Field[1].hwall_n = Delta0;
Field[1].hfar = 0.01;
Field[1].IntersectMetrics = 1;

BoundaryLayer Field = 1;

Extrude {0, 0, 10*scale} {
  Surface{1}; Layers {1}; Recombine;
}

Physical Surface("wallBottom",         444445) = {39, 43};
Physical Surface("wallShockGenerator", 444446) = {23};
Physical Surface("outlet",             444447) = {51};
Physical Surface("inlet",              444448) = {31};
Physical Surface("freeStream",         444449) = {27, 35, 55, 47};

Physical Volume(444450) = {1};
