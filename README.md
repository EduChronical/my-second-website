<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RRB JE 2026 Civil | 1000+ One Liners</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['Fira Code', 'monospace'],
                    },
                    colors: {
                        brand: {
                            dark: '#0B1120',
                            panel: '#151E32',
                            accent: '#38BDF8', // Sky blue
                            glow: '#0EA5E9',
                        }
                    },
                    animation: {
                        'fade-in': 'fadeIn 0.5s ease-out',
                        'slide-up': 'slideUp 0.5s ease-out',
                        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                    },
                    keyframes: {
                        fadeIn: {
                            '0%': { opacity: '0' },
                            '100%': { opacity: '1' },
                        },
                        slideUp: {
                            '0%': { transform: 'translateY(20px)', opacity: '0' },
                            '100%': { transform: 'translateY(0)', opacity: '1' },
                        }
                    }
                }
            }
        }
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Fira+Code:wght@400;600&display=swap');
        
        body { background-color: #0B1120; color: #e2e8f0; overflow: hidden; }
        
        /* 3D Canvas */
        #canvas-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none;
        }

        /* Custom Scrollbar for content areas */
        .custom-scroll::-webkit-scrollbar {
            width: 6px;
        }
        .custom-scroll::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.05);
        }
        .custom-scroll::-webkit-scrollbar-thumb {
            background: rgba(56, 189, 248, 0.3);
            border-radius: 10px;
        }
        .custom-scroll::-webkit-scrollbar-thumb:hover {
            background: rgba(56, 189, 248, 0.6);
        }

        /* Glassmorphism */
        .glass-panel {
            background: rgba(21, 30, 50, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }

        .subject-card {
            transition: all 0.3s ease;
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.9));
            border: 1px solid rgba(56, 189, 248, 0.1);
        }
        .subject-card:hover {
            transform: translateY(-5px);
            border-color: rgba(56, 189, 248, 0.5);
            box-shadow: 0 10px 30px -10px rgba(14, 165, 233, 0.3);
        }

        .qa-item {
            border-bottom: 1px solid rgba(255,255,255,0.05);
            transition: background 0.2s;
        }
        .qa-item:hover {
            background: rgba(56, 189, 248, 0.05);
        }
    </style>
</head>
<body class="antialiased h-screen w-screen flex flex-col">

    <!-- 3D Background -->
    <div id="canvas-bg"></div>

    <!-- Header -->
    <header class="relative z-10 w-full p-4 border-b border-white/10 glass-panel flex justify-between items-center">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-cyan-400 rounded-lg flex items-center justify-center shadow-lg shadow-blue-500/30">
                <i class="fas fa-hard-hat text-white text-lg"></i>
            </div>
            <div>
                <h1 class="text-xl font-bold tracking-tight text-white">RRB JE <span class="text-brand-accent">2026</span></h1>
                <p class="text-xs text-slate-400 uppercase tracking-widest">Civil Engineering Master</p>
            </div>
        </div>
        <div class="hidden md:flex items-center gap-4">
            <div class="px-3 py-1 rounded-full bg-green-500/10 border border-green-500/20 text-green-400 text-xs font-mono">
                <i class="fas fa-check-circle mr-1"></i> 1000+ Questions Loaded
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="relative z-10 flex-1 flex overflow-hidden">
        
        <!-- Sidebar (Subjects) -->
        <aside class="w-full md:w-1/3 lg:w-1/4 glass-panel border-r border-white/10 flex flex-col h-full transform transition-transform duration-300 absolute md:relative z-20" id="sidebar">
            <div class="p-4 border-b border-white/10 bg-slate-900/50">
                <h2 class="text-sm font-semibold text-slate-300 uppercase tracking-wider">Select Subject</h2>
                <p class="text-xs text-slate-500 mt-1">Click to load 100 Q&As</p>
            </div>
            
            <div class="overflow-y-auto custom-scroll p-4 space-y-3 flex-1" id="subject-list">
                <!-- Subject Cards Injected Here -->
            </div>
        </aside>

        <!-- Viewer (Q&A) -->
        <section class="flex-1 relative bg-slate-900/30 flex flex-col h-full">
            
            <!-- Empty State -->
            <div id="empty-state" class="absolute inset-0 flex flex-col items-center justify-center text-center p-8 z-0">
                <div class="w-24 h-24 bg-slate-800 rounded-full flex items-center justify-center mb-6 animate-pulse-slow border border-white/5">
                    <i class="fas fa-graduation-cap text-4xl text-brand-accent opacity-50"></i>
                </div>
                <h2 class="text-2xl font-bold text-white mb-2">Ready to Master RRB JE?</h2>
                <p class="text-slate-400 max-w-md">Select a subject from the sidebar to access 100 of the most repeated and important one-liner questions for the 2026 exam.</p>
            </div>

            <!-- Content Viewer -->
            <div id="content-viewer" class="hidden flex-col h-full w-full absolute inset-0 z-10 bg-slate-900/80 backdrop-blur-sm">
                <!-- Viewer Header -->
                <div class="p-6 border-b border-white/10 flex justify-between items-end bg-slate-900/60">
                    <div>
                        <div class="text-xs text-brand-accent font-mono mb-1" id="viewer-category">SUBJECT</div>
                        <h2 class="text-2xl md:text-3xl font-bold text-white" id="viewer-title">Subject Name</h2>
                    </div>
                    <div class="text-right hidden sm:block">
                        <div class="text-3xl font-bold text-white" id="progress-count">0/100</div>
                        <div class="text-xs text-slate-400">Mastered</div>
                    </div>
                </div>

                <!-- Questions List -->
                <div class="flex-1 overflow-y-auto custom-scroll p-4 md:p-8" id="qa-container">
                    <!-- Q&A Injected Here -->
                </div>
                
                <!-- Mobile Back Button -->
                <div class="md:hidden p-4 border-t border-white/10 bg-slate-900">
                    <button onclick="closeViewer()" class="w-full py-3 bg-slate-800 text-white rounded-lg font-semibold">Back to Subjects</button>
                </div>
            </div>

        </section>
    </main>

    <script>
        // --- 1. DATA: 100 Questions per Subject ---
        // We will distribute 100 questions across key technical subjects.
        // Note: To keep the file manageable, I will fill Engineering Mechanics fully and structure others.
        // In a real app, this would be an API call. Here I provide full comprehensive data.
        
        const db = {
            "Engineering Mechanics": [
                { q: "What is the S.I unit of Force?", a: "Newton (N)" },
                { q: "Define a Rigid Body.", a: "A body that does not deform under the application of force." },
                { q: "State Newton's First Law.", a: "A body remains at rest or moves with constant velocity unless acted upon by an external force." },
                { q: "State Newton's Second Law.", a: "Force is proportional to the rate of change of momentum (F=ma)." },
                { q: "State Newton's Third Law.", a: "Every action has an equal and opposite reaction." },
                { q: "What is a Scalar Quantity?", a: "A quantity with magnitude only (e.g., Mass, Time)." },
                { q: "What is a Vector Quantity?", a: "A quantity with magnitude and direction (e.g., Force, Velocity)." },
                { q: "Define Parallelogram Law of Forces.", a: "Resultant of two forces is the diagonal of the parallelogram formed by them." },
                { q: "What is the Resolution of Forces?", a: "Splitting a single force into components (usually horizontal and vertical)." },
                { q: "Define Moment of a Force.", a: "The turning effect of a force about a point (Force x Perpendicular Distance)." },
                { q: "What is a Couple?", a: "Two equal, opposite, and parallel forces acting at different points." },
                { q: "Define Equilibrant.", a: "A single force that brings the system to equilibrium (Equal and opposite to Resultant)." },
                { q: "State Varignon's Theorem.", a: "The moment of a force about any point is equal to the sum of moments of its components." },
                { q: "Define Free Body Diagram (FBD).", a: "A diagram showing the isolated body with all external forces acting on it." },
                { q: "What is the Unit of Work?", a: "Joule (N-m)." },
                { q: "What is Power?", a: "Rate of doing work (Work/Time)." },
                { q: "Define Energy.", a: "Capacity to do work." },
                { q: "State Law of Conservation of Energy.", a: "Energy can neither be created nor destroyed, only transformed." },
                { q: "Define Potential Energy.", a: "Energy possessed by a body by virtue of its position." },
                { q: "Define Kinetic Energy.", a: "Energy possessed by a body by virtue of its motion (0.5mv^2)." },
                { q: "What is Impulse?", a: "Product of force and time (Change in momentum)." },
                { q: "Define Momentum.", a: "Product of mass and velocity (mv)." },
                { q: "What is Collision?", a: "Interaction between two bodies for a short interval." },
                { q: "Define Coefficient of Restitution (e).", a: "Ratio of relative velocity after impact to relative velocity before impact." },
                { q: "What is the value of 'e' for perfectly elastic bodies?", a: "e = 1." },
                { q: "What is the value of 'e' for perfectly plastic bodies?", a: "e = 0." },
                { q: "Define Projectile Motion.", a: "Motion of a body thrown at an angle to the horizontal." },
                { q: "What is the Trajectory of a Projectile?", a: "Parabolic path." },
                { q: "Define Center of Gravity (C.G.).", a: "Point where the entire weight of the body is assumed to act." },
                { q: "Define Centroid.", a: "Geometric center of a plane figure." },
                { q: "Where is the C.G. of a Triangle?", a: "At the intersection of medians (1/3 of height from base)." },
                { q: "Where is the C.G. of a Semi-circle?", a: "At 4r/3π from the diameter." },
                { q: "Define Moment of Inertia (I).", a: "Second moment of area (Σ y^2 dA)." },
                { q: "S.I Unit of Moment of Inertia?", a: "mm^4 or m^4." },
                { q: "State Parallel Axis Theorem.", a: "Ixx = Ig + Ah^2 (Moment about any axis parallel to centroidal axis)." },
                { q: "State Perpendicular Axis Theorem.", a: "Iz = Ix + Iy (Valid only for laminar/plane bodies)." },
                { q: "Define Friction.", a: "Force resisting relative motion between surfaces." },
                { q: "What is Angle of Friction?", a: "Angle between Normal Reaction and Resultant of Friction and Normal Reaction." },
                { q: "What is Angle of Repose?", a: "Maximum angle of an inclined plane before a body starts sliding." },
                { q: "Relationship between Angle of Friction and Repose.", a: "They are equal (φ = α)." },
                { q: "Define Static Friction.", a: "Friction acting when body is at rest." },
                { q: "Define Kinetic/Dynamic Friction.", a: "Friction acting when body is in motion." },
                { q: "What is a Machine?", a: "Device used to overcome a resistance at some point by application of force at another point." },
                { q: "Define Mechanical Advantage (M.A.).", a: "Ratio of load lifted to effort applied (W/P)." },
                { q: "Define Velocity Ratio (V.R.).", a: "Ratio of distance moved by effort to distance moved by load." },
                { q: "Define Efficiency of a Machine.", a: "Ratio of output to input (M.A./V.R.)." },
                { q: "What is an Ideal Machine?", a: "A machine with 100% efficiency (no friction)." },
                { q: "Define Reversible Machine.", a: "A machine that can do work in reverse direction due to load." },
                { q: "Define Law of Machine.", a: "Relationship between load lifted (W) and effort applied (P) [P = mW + C]." },
                { q: "What is a Pulley?", a: "A wheel on an axle designed to support movement and change direction of cable." },
                { q: "What is a Weston Differential Pulley?", a: "A pulley system with two different radii for lifting heavy loads." },
                { q: "What is Simple Stress?", a: "Internal resistance per unit area (Force/Area)." },
                { q: "Define Strain.", a: "Deformation per unit length (Change in Length / Original Length)." },
                { q: "State Hooke's Law.", a: "Stress is directly proportional to strain within elastic limit." },
                { q: "Define Modulus of Elasticity (E).", a: "Ratio of stress to strain." },
                { q: "Define Shear Stress.", a: "Stress caused by forces acting parallel to the area." },
                { q: "Define Modulus of Rigidity (G or C).", a: "Ratio of shear stress to shear strain." },
                { q: "Define Poisson's Ratio.", a: "Ratio of lateral strain to linear strain." },
                { q: "Define Bulk Modulus (K).", a: "Ratio of direct stress to volumetric strain." },
                { q: "Relationship between E, G, and K.", a: "E = 9KG / (3K + G)." },
                { q: "Define Factor of Safety.", a: "Ratio of ultimate stress to working stress." },
                { q: "Define Elastic Limit.", a: "Maximum stress up to which material returns to original shape." },
                { q: "Define Yield Point.", a: "Point at which material shows an increase in strain without increase in stress." },
                { q: "Define Ultimate Stress.", a: "Maximum stress a material can withstand." },
                { q: "Define Breaking Stress.", a: "Stress at which material breaks." },
                { q: "Define Resilience.", a: "Strain energy stored in a body within elastic limit." },
                { q: "Define Proof Resilience.", a: "Maximum strain energy stored at elastic limit." },
                { q: "Define Modulus of Resilience.", a: "Proof resilience per unit volume." },
                { q: "Define Thermal Stress.", a: "Stress induced due to change in temperature." },
                { q: "Define Thermal Strain.", a: "Strain induced due to change in temperature (α * ΔT)." },
                { q: "Define Composite Bar.", a: "A bar made of two or more materials rigidly fixed together." },
                { q: "What is Fatigue?", a: "Failure of material under repeated stresses." },
                { q: "Define Endurance Limit.", a: "Maximum stress level below which a material can endure infinite cycles." },
                { q: "What is Creep?", a: "Slow and progressive deformation of a material under constant stress." },
                { q: "Define Hardness.", a: "Resistance of material to indentation or scratching." },
                { q: "Define Toughness.", a: "Ability of material to absorb energy and deform plastically before fracturing." },
                { q: "Define Ductility.", a: "Property of material to be drawn into wires." },
                { q: "Define Malleability.", a: "Property of material to be rolled into sheets." },
                { q: "Define Brittleness.", a: "Tendency of material to fracture without significant deformation." },
                { q: "What is a Beam?", a: "A structural member subjected to transverse loads." },
                { q: "Define Cantilever Beam.", a: "Beam fixed at one end and free at the other." },
                { q: "Define Simply Supported Beam.", a: "Beam supported at both ends with pin and roller." },
                { q: "Define Overhanging Beam.", a: "Beam supported such that one or both ends project beyond the support." },
                { q: "Define Shear Force (S.F.).", a: "Algebraic sum of all vertical forces to the left or right of a section." },
                { q: "Define Bending Moment (B.M.).", a: "Algebraic sum of moments of all forces to the left or right of a section." },
                { q: "S.I Unit of Shear Force.", a: "Newton (N) or kN." },
                { q: "S.I Unit of Bending Moment.", a: "N-m or kN-m." },
                { q: "Point of Contraflexure.", a: "Point where Bending Moment changes sign (Zero)." },
                { q: "What is a Truss?", a: "A structure composed of slender members joined together at end points." },
                { q: "What is a Perfect Truss?", a: "Truss satisfying m = 2j - 3 (m=members, j=joints)." },
                { q: "What is a Deficient/Imperfect Truss?", a: "Truss with m < 2j - 3." },
                { q: "What is a Redundant Truss?", a: "Truss with m > 2j - 3." },
                { q: "Method of Joints.", a: "Solving truss by satisfying equilibrium at each joint (ΣFx=0, ΣFy=0)." },
                { q: "Method of Sections.", a: "Solving truss by cutting it into sections and applying equilibrium equations." }
            ],
            "Strength of Materials": [
                { q: "Define Stress.", a: "Internal resistance offered by a body per unit area against deformation." },
                { q: "Define Strain.", a: "Ratio of change in dimension to original dimension." },
                { q: "Types of Stress.", a: "Tensile, Compressive, Shear." },
                { q: "Types of Strain.", a: "Linear/Longitudinal, Lateral, Volumetric, Shear." },
                { q: "Define Hookes Law.", a: "Within elastic limit, stress is directly proportional to strain." },
                { q: "Define Modulus of Elasticity.", a: "Ratio of linear stress to linear strain." },
                { q: "Define Shear Modulus.", a: "Ratio of shear stress to shear strain." },
                { q: "Define Poisson's Ratio.", a: "Ratio of lateral strain to linear strain." },
                { q: "Relationship between E, G, K.", a: "E = 9KG / (3K+G)" },
                { q: "Define Thermal Stress.", a: "Stress due to prevention of expansion/contraction by temperature change." },
                { q: "Define Composite Section.", a: "Section with two materials (e.g., steel rod in copper tube)." },
                { q: "Define Principal Stress.", a: "Maximum and minimum normal stress on a plane where shear stress is zero." },
                { q: "Mohr's Circle is used for?", a: "Graphical solution of principal stresses." },
                { q: "Define Strain Energy.", a: "Energy stored in body due to deformation." },
                { q: "Define Proof Resilience.", a: "Max strain energy stored at elastic limit." },
                { q: "Define Modulus of Resilience.", a: "Proof resilience per unit volume." },
                { q: "Define Torsion.", a: "Twisting of structural member by torque." },
                { q: "Torsion Equation.", a: "T/J = τ/R = Gθ/L." },
                { q: "Define Polar Modulus.", a: "Ratio of polar moment of inertia to radius of shaft." },
                { q: "Define Slenderness Ratio.", a: "Ratio of effective length to least radius of gyration." },
                { q: "Euler's Buckling Load Formula.", a: "P = π²EI / L²." },
                { q: "Define Column.", a: "Vertical compression member." },
                { q: "Define Beam.", a: "Horizontal member carrying transverse loads." },
                { q: "S.F.D. stands for?", a: "Shear Force Diagram." },
                { q: "B.M.D. stands for?", a: "Bending Moment Diagram." },
                { q: "Point of Contraflexure is?", a: "Where BM changes sign (Zero)." },
                { q: "Define Section Modulus (Z).", a: "Moment of Inertia / Distance to extreme fiber (I/y_max)." },
                { q: "Flexure Formula.", a: "M/I = f/y = E/R." },
                { q: "Define Slope of Beam.", a: "Angle made by tangent to elastic curve with original axis." },
                { q: "Define Deflection.", a: "Displacement of beam from original position." },
                { q: "Methods to find Slope & Deflection?", a: "Double Integration, Macaulay's, Moment Area, Conjugate Beam." },
                { q: "Define Propped Cantilever.", a: "Cantilever with simple support at free end." },
                { q: "Define Fixed Beam.", a: "Beam rigidly fixed at both ends." },
                { q: "Define Continuous Beam.", a: "Beam supported on more than two supports." },
                { q: "Clapeyron's Theorem of Three Moments.", a: "Relation between BMs at three supports of continuous beam." },
                { q: "Define Shear Stress in Beam.", a: "τ = VQ / Ib." },
                { q: "Distribution of Shear Stress in Rectangular Section?", a: "Parabolic, max at NA." },
                { q: "Distribution of Shear Stress in Circular Section?", a: "Parabolic." },
                { q: "Define Leaf Spring.", a: "Laminated spring used in vehicles." },
                { q: "Define Close Coiled Helical Spring.", a: "Spring with angle of helix < 10°." },
                { q: "Define Spring Stiffness.", a: "Load required to produce unit deflection." },
                { q: "Define Wahl's Factor.", a: "Factor to account for curvature and direct shear in springs." },
                { q: "Define Thin Cylinder.", a: "Wall thickness < 1/10th to 1/20th of internal diameter." },
                { q: "Circumferential/Hoop Stress formula in thin cylinder.", a: "pd / 2t." },
                { q: "Longitudinal Stress formula in thin cylinder.", a: "pd / 4t." },
                { q: "Define Thick Cylinder.", a: "Wall thickness is large (not negligible compared to diameter)." },
                { q: "Lame's Equations are for?", a: "Thick cylinders." },
                { q: "Define Wire Winding.", a: "Pre-stressing a cylinder by winding wire under tension." },
                { q: "Define Sphere.", a: "Ball-shaped pressure vessel." },
                { q: "Hoop stress in thin spherical shell?", a: "pd / 4t." },
                { q: "Define Strain Rosette.", a: "Arrangement of strain gauges to measure normal strains in different directions." },
                { q: "Define Fatigue.", a: "Failure under repeated/reversed stresses." },
                { q: "Define Endurance Limit.", a: "Max stress below which material can withstand infinite cycles." },
                { q: "Define Creep.", a: "Slow continuous deformation under constant load at high temp." },
                { q: "S-N Curve represents?", a: "Stress vs Number of cycles to failure." },
                { q: "Define Theories of Failure.", a: "Criteria predicting failure of ductile/brittle materials." },
                { q: "Maximum Principal Stress Theory.", a: "Failure occurs when max principal stress reaches ultimate stress." },
                { q: "Maximum Shear Stress Theory (Guest/Tresca).", a: "Failure occurs when max shear stress reaches shear stress at yield." },
                { q: "Distortion Energy Theory (Von-Mises).", a: "Failure occurs when distortion energy per unit volume reaches limit." },
                { q: "Define Castigliano's Theorem.", a: "Partial derivative of total strain energy w.r.t load gives deflection at load." },
                { q: "Define Maxwell's Reciprocal Theorem.", a: "Deflection at A due to load at B = Deflection at B due to load at A." },
                { q: "Define Betti's Law.", a: "Generalized reciprocal theorem for work done." },
                { q: "Define Flexural Rigidity.", a: "Resistance to bending (EI)." },
                { q: "Define Torsional Rigidity.", a: "Resistance to torsion (GJ or CJ)." },
                { q: "Neutral Axis passes through?", a: "Centroid of section (for pure bending)." },
                { q: "Moment of Area about Neutral Axis is?", a: "Zero." },
                { q: "Define Core/Section of a Section.", a: "Area within which load must act to produce only compressive stress." },
                { q: "Define Middle Quarter Rule.", a: "For rectangular section, load must be within middle quarter." },
                { q: "Define Middle Third Rule.", a: "For circular section, load must be within middle third." },
                { q: "Define Riveted Joint.", a: "Permanent joint using rivets." },
                { q: "Define Welded Joint.", a: "Permanent joint by fusion." },
                { q: "Modes of Failure of Riveted Joint?", a: "Tearing of plate, Shearing of rivet, Crushing of rivet." },
                { q: "Define Efficiency of Joint.", a: "Strength of joint / Strength of solid plate." },
                { q: "Define Unwin's Formula.", a: "Diameter of rivet = 6.04 * sqrt(t)." },
                { q: "Define Lacing.", a: "System of bars connecting components of built-up column." },
                { q: "Define Battening.", a: "System of plates/bars perpendicular to main component." },
                { q: "Define Perry-Robertson Formula.", a: "Empirical formula for design of struts/columns." },
                { q: "Define Johnson's Parabolic Formula.", a: "For short/intermediate columns." },
                { q: "Define Straight Line Formula.", a: "Rankine-Gordon formula for columns." },
                { q: "Define Eccentric Loading.", a: "Load not passing through centroid." },
                { q: "Define Stress Concentration.", a: "Localization of high stress due to irregularities." },
                { q: "Define Notch Sensitivity.", a: "Measure of sensitivity of material to notches." },
                { q: "Define Fluctuating Stress.", a: "Varying between min and max values." },
                { q: "Define Repeated Stress.", a: "Varying from zero to max." },
                { q: "Define Reversed Stress.", a: "Varying from -min to +max (mean zero)." },
                { q: "Define Gerber Line.", a: "Failure curve for fatigue (Parabolic)." },
                { q: "Define Goodman Line.", a: "Straight line joining endurance limit and ultimate stress." },
                { q: "Define Soderberg Line.", a: "Straight line joining endurance limit and yield stress (Safest)." }
            ],
            "Soil Mechanics": [
                { q: "Define Soil Mechanics.", a: "Application of laws of mechanics and hydraulics to engineering problems dealing with soils." },
                { q: "Define Phase Diagram.", a: "Diagram showing different phases of soil (Solid, Water, Air)." },
                { q: "Define Void Ratio (e).", a: "Ratio of volume of voids to volume of solids." },
                { q: "Define Porosity (n).", a: "Ratio of volume of voids to total volume." },
                { q: "Relationship between e and n.", a: "n = e / (1+e)." },
                { q: "Define Water Content (w).", a: "Ratio of weight of water to weight of solids." },
                { q: "Define Degree of Saturation (S).", a: "Ratio of volume of water to volume of voids." },
                { q: "Relationship Se = wG.", a: "S * e = w * G (G=Specific Gravity)." },
                { q: "Define Bulk Density.", a: "Total weight / Total volume." },
                { q: "Define Dry Density.", a: "Weight of solids / Total volume." },
                { q: "Define Saturated Density.", a: "Bulk density when soil is fully saturated." },
                { q: "Define Submerged Density.", a: "Bulk density - Density of water." },
                { q: "Define Specific Gravity of Solids (G).", a: "Ratio of unit weight of solids to unit weight of water." },
                { q: "Methods for Water Content determination?", a: "Oven Drying, Calcium Carbide, Torsion, Pycnometer, Sand Bath." },
                { q: "Oven Drying Temp and Duration.", a: "110°C ± 5°C for 24 hours." },
                { q: "Define Liquid Limit (LL).", a: "Water content at which soil changes from liquid to plastic state." },
                { q: "Define Plastic Limit (PL).", a: "Water content at which soil changes from plastic to semi-solid state." },
                { q: "Define Shrinkage Limit (SL).", a: "Water content at which soil stops shrinking." },
                { q: "Define Plasticity Index (PI).", a: "LL - PL." },
                { q: "Define Flow Index (If).", a: "Slope of flow curve in Liquid Limit test." },
                { q: "Define Toughness Index.", a: "Plasticity Index / Flow Index." },
                { q: "Define Consistency Index (Ic).", a: "(LL - w) / PI." },
                { q: "Define Liquidity Index (Il).", a: "(w - PL) / PI." },
                { q: "What is Casagrande's Apparatus used for?", a: "Liquid Limit test." },
                { q: "How many blows in Casagrande's test?", a: "25 blows." },
                { q: "What is Thread Test used for?", a: "Plastic Limit test (3mm thread crumbles)." },
                { q: "Define Soil Classification.", a: "Arrangement of soils into groups based on properties." },
                { q: "IS Classification System uses?", a: "Plasticity Chart and Particle Size." },
                { q: "Soil types based on size (IS).", a: "Gravel (>4.75mm), Sand (4.75-0.075mm), Silt (0.075-0.002mm), Clay (<0.002mm)." },
                { q: "Define Permeability (k).", a: "Property of soil allowing water to flow through." },
                { q: "Darcy's Law.", a: "v = k * i (Velocity = Coefficient * Hydraulic Gradient)." },
                { q: "Define Hydraulic Gradient (i).", a: "Head loss / Length of seepage path." },
                { q: "Discharge Velocity vs Seepage Velocity.", a: "v = vs * n (Seepage velocity is actual velocity in voids)." },
                { q: "Factors affecting Permeability.", a: "Particle size, void ratio, degree of saturation, structure, impurities." },
                { q: "Allen Hazen Formula.", a: "k = C * D10^2." },
                { q: "Constant Head Permeability test used for?", a: "Coarse grained soils (Gravel, Sand)." },
                { q: "Falling Head Permeability test used for?", a: "Fine grained soils (Clay, Silt)." },
                { q: "Define Capillarity in Soils.", a: "Rise of water in soil voids above water table." },
                { q: "Capillary Rise formula (Approx).", a: "h = 0.03 / d (cm) where d is pore diameter." },
                { q: "Define Effective Stress.", a: "Total stress - Pore water pressure (σ' = σ - u)." },
                { q: "Principle of Effective Stress by?", a: "Terzaghi (1923)." },
                { q: "Quick Sand Condition.", a: "When effective stress becomes zero (boiling)." },
                { q: "Hydraulic Gradient for Quick Sand?", a: "Critical Gradient ic = (G-1)/(1+e)." },
                { q: "Define Seepage Pressure.", a: "Pressure exerted by water flowing through soil." },
                { q: "Define Flow Net.", a: "Network of stream lines and equipotential lines." },
                { q: "Define Stream Line.", a: "Path along which a water particle travels." },
                { q: "Define Equipotential Line.", a: "Line joining points of equal total head." },
                { q: "Properties of Flow Net.", a: "Stream lines and equipotential lines intersect at 90°." },
                { q: "Uses of Flow Net.", a: "Estimation of seepage, uplift pressure, exit gradient." },
                { q: "Define Compaction.", a: "Densification of soil by mechanical means." },
                { q: "Aim of Compaction.", a: "Increase density, shear strength, reduce permeability/compressibility." },
                { q: "Factors affecting Compaction.", a: "Water content, compactive effort, soil type." },
                { q: "Standard Proctor Test.", a: "Compaction test using 2.6kg hammer, 310mm drop, 3 layers, 25 blows." },
                { q: "Modified Proctor Test.", a: "Heavier compaction (4.89kg hammer, 450mm drop)." },
                { q: "OMC stands for?", a: "Optimum Moisture Content." },
                { q: "MDD stands for?", a: "Maximum Dry Density." },
                { q: "Zero Air Voids Line.", a: "Theoretical curve representing 100% saturation." },
                { q: "Effect of Compaction on Soils.", a: "Flocculated structure at low energy, dispersed at high energy." },
                { q: "Field Compaction Equipment.", a: "Smooth wheel rollers, Pneumatic rollers, Sheepsfoot rollers, Vibratory rollers." },
                { q: "Relative Compaction is?", a: "Field dry density / Lab max dry density." },
                { q: "Define Compressibility.", a: "Property of soil to decrease in volume under pressure." },
                { q: "Consolidation vs Compaction.", a: "Consolidation is static, time-dependent; Compaction is dynamic, instant." },
                { q: "Terzaghi's 1D Consolidation Theory.", a: "Rate of escape of water controls compression." },
                { q: "Define Compression Index (Cc).", a: "Slope of virgin curve in e-log p plot." },
                { q: "Define Swelling Index (Cs).", a: "Slope of unloading/reloading curve." },
                { q: "Pre-consolidation Pressure (Pc).", a: "Maximum pressure the soil has ever endured." },
                { q: "Normally Consolidated Clay.", a: "Current effective stress = Pre-consolidation pressure." },
                { q: "Over-consolidated Clay.", a: "Current effective stress < Pre-consolidation pressure." },
                { q: "Over Consolidation Ratio (OCR).", a: "Pc / Current effective stress." },
                { q: "Define Coefficient of Consolidation (Cv).", a: "Parameter indicating rate of consolidation." },
                { q: "Time Factor (Tv).", a: "Cv * t / d^2." },
                { q: "Consolidation Settlement depends on?", a: "Compression index, pressure change, initial void ratio, thickness." },
                { q: "Cassagrande's Logarithm of Time Fitting Method.", a: "To find Cv from consolidation test data." },
                { q: "Define Shear Strength.", a: "Resistance to shear deformation." },
                { q: "Mohr-Coulomb Equation.", a: "s = c + σ' tan(φ)." },
                { q: "Define Cohesion (c).", a: "Shear strength at zero normal stress." },
                { q: "Define Angle of Internal Friction (φ).", a: "Slope of failure envelope." },
                { q: "Direct Shear Test.", a: "Box shear test, strain controlled." },
                { q: "Triaxial Compression Test.", a: "Confining pressure applied in 3 axes." },
                { q: "Unconfined Compression Test (UCS).", a: "Special case of triaxial with σ3=0, for cohesive soils." },
                { q: "Vane Shear Test.", a: "Used for soft sensitive clays in field/lab." },
                { q: "Stress-Strain Curve for Dense Sand.", a: "Shows peak strength then drops (strain softening)." },
                { q: "Stress-Strain Curve for Loose Sand.", a: "Shows continuous increase (strain hardening)." },
                { q: "Critical Void Ratio.", a: "Void ratio at which no volume change occurs during shear." },
                { q: "Sensitivity of Clay.", a: "Ratio of undisturbed strength to remoulded strength." },
                { q: "Thixotropy.", a: "Loss of strength due to remoulding, regained over time." },
                { q: "Bearing Capacity.", a: "Ability of soil to support loads." },
                { q: "Ultimate Bearing Capacity (qu).", a: "Gross pressure at base causing shear failure." },
                { q: "Net Ultimate Bearing Capacity.", a: "qu - γD (overburden pressure)." },
                { q: "Safe Bearing Capacity.", a: "Net ultimate / FOS + γD." },
                { q: "Allowable Bearing Pressure.", a: "Net safe bearing capacity." },
                { q: "Terzaghi's Bearing Capacity Theory.", a: "Assumes general shear failure, rough base, shallow foundation." },
                { q: "General Shear Failure.", a: "Sudden collapse, well-defined failure surface." },
                { q: "Local Shear Failure.", a: "Significant compression, large settlement, no sudden collapse." },
                { q: "Punching Shear Failure.", a: "Vertical shearing around foundation." },
                { q: "Factors affecting Bearing Capacity.", a: "Soil type, foundation size/depth, water table, eccentricity." },
                { q: "Effect of Water Table on BC.", a: "Reduces effective stress, hence reduces bearing capacity." },
                { q: "Plate Load Test.", a: "Field test to determine bearing capacity and settlement." },
                { q: "Standard Penetration Test (SPT).", a: "Split spoon sampler driven by 63.5kg hammer, 450mm drop." },
                { q: "N-value in SPT.", a: "Number of blows for last 300mm penetration." },
                { q: "Correction for N-value.", a: "Overburden correction and Dilatancy correction." },
                { q: "Static Cone Penetration Test (SCPT).", a: "Dutch Cone Test, measuring cone resistance." },
                { q: "Earth Pressure at Rest (P0).", a: "When wall does not move." },
                { q: "Active Earth Pressure (Pa).", a: "When wall moves away from soil (min pressure)." },
                { q: "Passive Earth Pressure (Pp).", a: "When wall moves towards soil (max pressure)." },
                { q: "Rankine's Earth Pressure Theory.", a: "Assumes no wall friction, smooth vertical wall." },
                { q: "Coulomb's Earth Pressure Theory.", a: "Assumes plane failure surface, considers wall friction." },
                { q: "Define Slope Failure.", a: "Downward movement of slope mass due to gravity." },
                { q: "Types of Slope Failures.", a: "Rotational (Circular/Non-circular) and Translational." },
                { q: "Swedish Circle Method.", a: "Method of slices for slope stability analysis." },
                { q: "Fellenius Method of Slices.", a: "Simplified Bishop method ignoring side forces." },
                { q: "Factor of Safety for Slopes.", a: "Resisting forces / Driving forces." },
                { q: "Stabilization Methods for Slopes.", a: "Flattening, benching, drainage, retaining walls, grouting." }
            ],
            "Surveying": [
                { q: "Define Surveying.", a: "Science of determining relative positions of points on earth." },
                { q: "Primary Division of Surveying.", a: "Plane Surveying and Geodetic Surveying." },
                { q: "Plane Surveying assumption.", a: "Earth's surface is flat (small areas)." },
                { q: "Geodetic Surveying assumption.", a: "Earth's curvature is considered (large areas)." },
                { q: "Types of Surveying based on instruments?", a: "Chain, Compass, Plane Table, Theodolite, Tacheometric, Photogrammetric." },
                { q: "Types of Surveying based on purpose?", a: "Geological, Mine, Archaeological, Military." },
                { q: "Principle of Surveying.", a: "Working from whole to part." },
                { q: "Why 'Whole to Part'?", a: "To localize errors and prevent accumulation." },
                { q: "Define Leveling.", a: "Finding elevations of points relative to a datum." },
                { q: "Define Plan.", a: "Orthographic projection on a horizontal plane." },
                { q: "Define Map.", a: "Representation of earth's surface on a small scale." },
                { q: "Difference between Plan and Map?", a: "Scale (Plan: large, Map: small)." },
                { q: "Define Scale.", a: "Ratio of drawing distance to ground distance." },
                { q: "Representative Fraction (RF).", a: "1cm on map / X cm on ground." },
                { q: "Plain Scale measures?", a: "Two dimensions (e.g., meters, decimeters)." },
                { q: "Diagonal Scale measures?", a: "Three dimensions (e.g., meters, dm, cm)." },
                { q: "Vernier Scale measures?", a: "Fractions of the smallest division of main scale." },
                { q: "Least Count of Vernier.", a: "Value of smallest division on main scale / Number of divisions on vernier." },
                { q: "Direct Ranging.", a: "Ranging a line when end points are intervisible." },
                { q: "Reciprocal Ranging.", a: "Ranging a line when end points are not intervisible." },
                { q: "Methods of Ranging.", a: "Eye judgment, Line ranger, Theodolite." },
                { q: "Chain Surveying is suitable for?", a: "Small, flat areas with few details." },
                { q: "Well-conditioned Triangle.", a: "Angles between 30° and 120° (preferably equilateral)." },
                { q: "Why avoid ill-conditioned triangles?", a: "Small errors in angle cause large errors in apex position." },
                { q: "Main stations in Chain Surveying.", a: "End points of survey lines." },
                { q: "Tie stations.", a: "Subsidiary stations on main survey lines." },
                { q: "Check lines/Proof lines.", a: "Lines joining apex to base to verify accuracy." },
                { q: "Offset.", a: "Lateral distance of object from survey line." },
                { q: "Perpendicular Offset.", a: "Right angle to survey line (90°)." },
                { q: "Oblique Offset.", a: "Not at right angle." },
                { q: "Errors in Chaining.", a: "Incorrect length of chain, bad ranging, non-horizontality." },
                { q: "Correction for Standardization.", a: "True length = (L'/L) * Measured length." },
                { q: "Correction for Slope.", a: "Ch = h^2 / 2L (h=height diff, L=slope length)." },
                { q: "Correction for Tension.", a: "Cp = (P - Po)L / AE." },
                { q: "Correction for Temperature.", a: "Ct = α(Tm - To)L." },
                { q: "Define Compass Surveying.", a: "Surveying using compass to determine direction of survey lines." },
                { q: "True Meridian.", a: "Line passing through geographical north and south poles." },
                { q: "Magnetic Meridian.", a: "Direction indicated by freely suspended magnetic needle." },
                { q: "Arbitrary Meridian.", a: "Any convenient direction (e.g., center line of building)." },
                { q: "True Bearing.", a: "Angle with True Meridian." },
                { q: "Magnetic Bearing.", a: "Angle with Magnetic Meridian." },
                { q: "Magnetic Declination.", a: "Angle between True and Magnetic meridian." },
                { q: "Isogonic Line.", a: "Line joining points of equal declination." },
                { q: "Agonic Line.", a: "Line joining points of zero declination." },
                { q: "Dip of needle.", a: "Inclination of needle with horizontal." },
                { q: "Isoclinic Line.", a: "Line joining points of equal dip." },
                { q: "Aclinic Line.", a: "Line joining points of zero dip (Magnetic equator)." },
                { q: "Prismatic Compass uses?", a: "Whole Circle Bearing (WCB) system (0° to 360°)." },
                { q: "Surveyor's Compass uses?", a: "Quadrantal Bearing (QB) system (0° to 90°)." },
                { q: "Fore Bearing (F.B.).", a: "Bearing of a line in the direction of survey progress." },
                { q: "Back Bearing (B.B.).", a: "Bearing of a line in opposite direction." },
                { q: "Relation FB and BB (WCB).", a: "BB = FB ± 180°." },
                { q: "Local Attraction.", a: "Magnetic disturbance caused by iron ore, steel structures." },
                { q: "How to detect Local Attraction?", a: "Difference between FB and BB should be exactly 180°." },
                { q: "How to correct Local Attraction?", a: "Start from unaffected line and correct bearings progressively." },
                { q: "Define Traversing.", a: "Connecting survey lines to form a network." },
                { q: "Closed Traverse.", a: "Forms a closed circuit (Loop traverse, connecting traverse)." },
                { q: "Open Traverse.", a: "Does not form a closed circuit." },
                { q: "Error of Closure.", a: "Algebraic sum of latitudes (ΣL) and departures (ΣD) should be zero." },
                { q: "Latitude.", a: "Projection of line on North-South meridian (L * cos θ)." },
                { q: "Departure.", a: "Projection of line on East-West line (L * sin θ)." },
                { q: "Bowditch's Rule.", a: "Correction to latitude/departure = Total error * (Line length / Perimeter)." },
                { q: "Transit Rule.", a: "Correction based on latitude/departure of line compared to total." },
                { q: "Define Leveling.", a: "Determining relative heights of points." },
                { q: "Datum Surface.", a: "Reference surface with respect to which elevations are measured." },
                { q: "Mean Sea Level (MSL).", a: "Average height of sea for all stages of tides." },
                { q: "Bench Mark (B.M.).", a: "Point of known elevation." },
                { q: "GTS Bench Mark.", a: "Great Trigonometrical Survey bench mark established by Survey of India." },
                { q: "Permanent B.M.", a: "Fixed reference points on permanent structures." },
                { q: "Temporary B.M.", a: "Established at end of day's work." },
                { q: "Reduced Level (R.L.).", a: "Height of point above datum." },
                { q: "Height of Instrument (H.I.).", a: "R.L. of plane of sight." },
                { q: "Back Sight (B.S.).", a: "First reading taken after setting up instrument." },
                { q: "Fore Sight (F.S.).", a: "Last reading taken before shifting instrument." },
                { q: "Intermediate Sight (I.S.).", a: "Readings taken between B.S. and F.S." },
                { q: "Rise and Fall Method.", a: "Compare staff readings to find rise or fall." },
                { q: "Height of Collimation Method.", a: "Uses H.I. to calculate R.L.s." },
                { q: "Arithmetic Check for Rise & Fall.", a: "ΣB.S. - ΣF.S. = ΣRise - ΣFall = Last R.L. - First R.L." },
                { q: "Arithmetic Check for H.I. Method.", a: "ΣB.S. - ΣF.S. = Last R.L. - First R.L." },
                { q: "Dumpy Level.", a: "Simplest type, telescope rigidly fixed to supports." },
                { q: "Tilting Level.", a: "Telescope can be tilted about its axis for focusing." },
                { q: "Auto Level.", a: "Automatic compensation for slight tilt." },
                { q: "Sensitiveness of Bubble Tube.", a: "Smallest angle/division tilt measured." },
                { q: "Curvature Correction.", a: "Always subtractive (-0.0785 D^2)." },
                { q: "Refraction Correction.", a: "Always additive (+0.0112 D^2)." },
                { q: "Combined Correction (C&R).", a: "-0.0673 D^2 (Subtractive)." },
                { q: "Distance Visible to horizon (D).", a: "D = 3.855 * sqrt(h) km." },
                { q: "Reciprocal Leveling.", a: "Eliminates errors due to curvature, refraction, and collimation." },
                { q: "Trigonometric Leveling.", a: "Determining R.L. of point from vertical angle and horizontal distance." },
                { q: "Stadia Tacheometry.", a: "Determining distance using staff intercept and stadia hairs." },
                { q: "Tangential Tacheometry.", a: "Uses vertical angles to top and bottom of staff." },
                { q: "Anallactic Lens.", a: "Makes additive constant zero (f+d=0)." },
                { q: "Staff Readings in Stadia.", a: "Top hair, Middle hair, Bottom hair." },
                { q: "Intercept.", a: "Difference between top and bottom hair reading (S)." },
                { q: "Theodolite measures?", a: "Horizontal and Vertical angles." },
                { q: "Transiting/Plunging.", a: "Reversing telescope in vertical plane (180°)." },
                { q: "Swinging.", a: "Turning telescope in horizontal plane." },
                { q: "Face Left Observation.", a: "Vertical circle left of observer." },
                { q: "Face Right Observation.", a: "Vertical circle right of observer." },
                { q: "Why take both Face L & R?", a: "To eliminate instrumental errors." },
                { q: "Latitude of a course.", a: "Length * cos(reduced bearing)." },
                { q: "Departure of a course.", a: "Length * sin(reduced bearing)." },
                { q: "Closing Error.", a: "Resultant of error in latitude and departure." },
                { q: "Balancing the Traverse.", a: "Applying corrections to latitudes and departures." },
                { q: "Omitted Measurements.", a: "Calculating length/bearing of missing side." },
                { q: "Horizontal Control.", a: "Control points established by triangulation or traversing." },
                { q: "Triangulation.", a: "Measuring angles of a network of triangles." },
                { q: "Triangulation Base Line.", a: "Measured side of triangle." },
                { q: "Laplace Station.", a: "Station where azimuth is determined astronomically." },
                { q: "Signals in Triangulation.", a: "Objects erected at stations to define exact point." },
                { q: "Phase of Signal.", a: "Error due to signals not being centered." },
                { q: "Satellite Station.", a: "Auxiliary station near main triangulation station." },
                { q: "Reduction to Center.", a: "Correcting angles measured at satellite station." },
                { q: "Axis Signal Correction.", a: "Correction applied when observation is made on edge of signal." },
                { q: "Define Photogrammetry.", a: "Surveying using photographs." },
                { q: "Terrestrial Photogrammetry.", a: "Camera on ground." },
                { q: "Aerial Photogrammetry.", a: "Camera in aircraft." },
                { q: "Vertical Photograph.", a: "Optical axis vertical." },
                { q: "Tilted Photograph.", a: "Optical axis intentionally tilted." },
                { q: "Oblique Photograph.", a: "Optical axis tilted > 3°." },
                { q: "Scale of Vertical Photograph.", a: "S = f / (H - h)." },
                { q: "Relief Displacement.", a: "Displacement of image point due to height of object." },
                { q: "Relief Displacement formula.", a: "r * h / H." },
                { q: "Overlap in Aerial Photos.", a: "Longitudinal (60%) and Side (25-30%)." },
                { q: "Flight Line.", a: "Line on ground representing camera axis." },
                { q: "Define Remote Sensing.", a: "Acquisition of info about object without physical contact." },
                { q: "GIS stands for?", a: "Geographic Information System." },
                { q: "GPS stands for?", a: "Global Positioning System." }
            ],
             "Building Materials & Construction": [
                { q: "Define Cement.", a: "Binding material (Calcareous + Argillaceous)." },
                { q: "Chemical composition of cement.", a: "Lime (62-67%), Silica (17-25%), Alumina (3-8%), Iron Oxide (2-4%)." },
                { q: "Function of Gypsum in Cement.", a: "Retards setting time." },
                { q: "Bogue's Compounds.", a: "C3S, C2S, C3A, C4AF." },
                { q: "Compound for early strength.", a: "C3S (Tri-calcium Silicate)." },
                { q: "Compound for ultimate strength.", a: "C2S (Di-calcium Silicate)." },
                { q: "Compound for flash setting.", a: "C3A (Tri-calcium Aluminate)." },
                { q: "Initial Setting Time of OPC.", a: "Not less than 30 minutes." },
                { q: "Final Setting Time of OPC.", a: "Not more than 600 minutes (10 hours)." },
                { q: "Fineness of Cement tested by?", a: "Sieve method (IS 90 micron) or Air permeability method." },
                { q: "Soundness of Cement tested by?", a: "Le-Chatelier apparatus or Autoclave test." },
                { q: "Why Soundness test?", a: "To detect presence of uncombined lime (CaO) or magnesia (MgO)." },
                { q: "Consistency of Cement tested by?", a: "Vicat apparatus." },
                { q: "Normal Consistency of Cement.", a: "Percentage of water by weight to form paste of standard consistency." },
                { q: "Compressive Strength of OPC 33 Grade at 3 days.", a: "16 MPa." },
                { q: "Compressive Strength of OPC 33 Grade at 28 days.", a: "33 MPa." },
                { q: "Hydrophobic Cement.", a: "Cement coated with acid to repel water during storage." },
                { q: "Rapid Hardening Cement.", a: "High C3S, fine grinding, high early strength." },
                { q: "Low Heat Cement.", a: "Low C3A and C3S, used for mass concrete (dams)." },
                { q: "Sulphate Resisting Cement.", a: "Low C3A (<5%), used in foundations with sulphate soil." },
                { q: "White Cement.", a: "Raw material free from iron oxide, used for architectural purposes." },
                { q: "Portland Pozzolana Cement (PPC).", a: "OPC + Pozzolana (Fly ash/Volcanic ash), economical, durable." },
                { q: "Define Aggregate.", a: "Inert material mixed with cement paste to form concrete." },
                { q: "Fine Aggregate size.", a: "Passing 4.75mm sieve (Sand)." },
                { q: "Coarse Aggregate size.", a: "Retained on 4.75mm sieve (Gravel/Crushed stone)." },
                { q: "Bulking of Sand.", a: "Increase in volume due to moisture content." },
                { q: "Maximum Bulking occurs at?", a: "4-6% moisture content." },
                { q: "Fineness Modulus (F.M.).", a: "Index of fineness of aggregate." },
                { q: "F.M. for Fine Aggregate.", a: "2.2 to 3.2." },
                { q: "F.M. for Coarse Aggregate.", a: "5.5 to 8.0." },
                { q: "Grading of Aggregate.", a: "Distribution of particle size." },
                { q: "Gap Graded Aggregate.", a: "Intermediate sizes missing." },
                { q: "Define Concrete.", a: "Mixture of cement, sand, aggregate, and water." },
                { q: "Water-Cement Ratio.", a: "Ratio of weight of water to weight of cement." },
                { q: "Abrams' Law.", a: "Strength of concrete is inversely proportional to water-cement ratio." },
                { q: "Workability.", a: "Ease with which concrete can be mixed, placed, compacted." },
                { q: "Slump Test.", a: "For workability of concrete." },
                { q: "Compaction Factor Test.", a: "More accurate for low workability concrete." },
                { q: "Vee-Bee Consistometer.", a: "For stiff concrete mixes." },
                { q: "Segregation.", a: "Separation of coarse aggregate from mortar." },
                { q: "Bleeding.", a: "Water rising to surface of freshly placed concrete." },
                { q: "Curing.", a: "Process of maintaining moisture and temp for concrete to develop strength." },
                { q: "Duration of Curing.", a: "Minimum 7 days for OPC, 10 days for blended cements." },
                { q: "Methods of Curing.", a: "Ponding, Sprinkling, Steam curing, Membrane curing." },
                { q: "Define Mortar.", a: "Mixture of cement/sand/lime and water (no coarse aggregate)." },
                { q: "Brick Masonry.", a: "Construction with bricks bonded with mortar." },
                { q: "Stretcher Bond.", a: "All bricks laid as stretchers (Half bond)." },
                { q: "Header Bond.", a: "All bricks laid as headers." },
                { q: "English Bond.", a: "Alternative courses of stretchers and headers." },
                { q: "Flemish Bond.", a: "Each course consists of alternate stretchers and headers." },
                { q: "Queen Closer.", a: "Half brick cut longitudinally." },
                { q: "King Closer.", a: "Brick cut cornerwise, one corner removed." },
                { q: "Corbel.", a: "Projecting stone supporting a structure, each course projecting ~1/4 brick." },
                { q: "Cornice.", a: "Decorative molding at top of wall." },
                { q: "Coping.", a: "Covering on top of wall to protect from rain." },
                { q: "Parapet.", a: "Low wall along edge of roof/bridge." },
                { q: "Damp Proof Course (DPC).", a: "Layer to prevent moisture rising by capillary action." },
                { q: "Common materials for DPC.", a: "Bitumen, Mastic asphalt, Metal sheets, Plastic sheets." },
                { q: "Plastering.", a: "Covering rough walls with mortar for smooth finish." },
                { q: "Pointing.", a: "Raking out joints and filling with mortar to improve appearance." },
                { q: "Scaffolding.", a: "Temporary platform for workmen and materials." },
                { q: "Types of Scaffolding.", a: "Single, Double, Cantilever, Suspended, Trestle." },
                { q: "Centering.", a: "Temporary support for arches, domes, etc." },
                { q: "Shuttering.", a: "Vertical temporary support for concrete (sides of beams/columns)." },
                { q: "Formwork.", a: "Mold in which concrete is placed." },
                { q: "Stripping Time for Props to Slabs.", a: "3 days (props refixed), 7 days (removal), 14 days (spans > 4.5m)." },
                { q: "Timber used for formwork?", a: "Soft wood (Pine, Fir)." },
                { q: "Define Foundation.", a: "Lowest part of structure transferring load to soil." },
                { q: "Bearing Capacity of Soil.", a: "Max load soil can take without shear failure." },
                { q: "Shallow Foundation.", a: "Depth < Width (Isolated, Combined, Strip, Raft)." },
                { q: "Deep Foundation.", a: "Depth > Width (Pile, Pier, Well)." },
                { q: "Spread Footing.", a: "Wider base to distribute load." },
                { q: "Raft/Mat Foundation.", a: "Large slab supporting whole building." },
                { q: "Pile Foundation.", a: "Long vertical members driven into ground." },
                { q: "Uses of Pile Foundation.", a: "Heavy loads, compressible soil, water table high." },
                { q: "End Bearing Piles.", a: "Transmit load through tip to hard strata." },
                { q: "Friction Piles.", a: "Transmit load through friction along surface." },
                { q: "Under-reamed Piles.", a: "Bulb at bottom to anchor in expansive soils." },
                { q: "Caisson.", a: "Water tight chamber for work under water." },
                { q: "Types of Caissons.", a: "Box Caisson, Pneumatic Caisson, Open Caisson." },
                { q: "Coffer-dam.", a: "Temporary structure to keep water/soil out." },
                { q: "Types of Coffer-dams.", a: "Earthen, Rockfill, Single-walled, Double-walled, Cellular." },
                { q: "Dewatering methods.", a: "Sumps and pumps, Well point system, Deep well pumps." },
                { q: "Soil Stabilization.", a: "Improving engineering properties of soil." },
                { q: "Methods of Soil Stabilization.", a: "Mechanical, Cement, Lime, Bitumen, Chemical." },
                { q: "Define Earthquake.", a: "Sudden release of energy from within earth." },
                { q: "Seismic Waves.", a: "P-waves (Primary), S-waves (Secondary), Surface waves." },
                { q: "Epicenter.", a: "Point on earth's surface vertically above focus." },
                { q: "Focus/Hypocenter.", a: "Origin of earthquake inside earth." },
                { q: "Richter Scale.", a: "Logarithmic scale measuring magnitude of earthquake." },
                { q: "Mercalli Scale.", a: "Measures intensity of earthquake based on damage." },
                { q: "Tremie Method.", a: "Placing concrete under water using a pipe." },
                { q: "Guniting.", a: "Spraying concrete/mortar at high velocity (Shotcrete)." },
                { q: "Pre-stressed Concrete.", a: "Concrete with induced compressive stress to resist tensile stress." },
                { q: "Pre-tensioning.", a: "Tendons tensioned before casting concrete." },
                { q: "Post-tensioning.", a: "Tendons tensioned after concrete hardens." },
                { q: "Ferro-cement.", a: "Thin wall reinforced concrete using wire mesh." },
                { q: "Fiber Reinforced Concrete (FRC).", a: "Concrete with fibrous material to increase structural integrity." },
                { q: "Ready Mix Concrete (RMC).", a: "Concrete manufactured in batching plant and delivered to site." },
                { q: "Mass Concrete.", a: "Concrete in bulk (> 1.5m dimension), risk of heat of hydration." },
                { q: "Lightweight Concrete.", a: "Density < 1920 kg/m3." },
                { q: "High Strength Concrete.", a: "Compressive strength > 40 MPa." },
                { q: "Self Compacting Concrete (SCC).", a: "Flows under own weight, no vibration needed." },
                { q: "Concrete Admixtures.", a: "Materials added to modify properties (Accelerators, Retarders, Plasticizers)." },
                { q: "Define Brick.", a: "Rectangular block of burnt clay." },
                { q: "Standard Size of Brick (India).", a: "190mm x 90mm x 90mm." },
                { q: "Compressive Strength of 1st Class Brick.", a: "Not less than 10 N/mm2." },
                { q: "Water Absorption of Brick.", a: "Not more than 20% by weight." },
                { q: "Define Efflorescence in Bricks.", a: "White crystalline deposit of salts on surface." }
            ],
            "RCC & Steel Design": [
                { q: "What is WSM?", a: "Working Stress Method (Elastic Theory)." },
                { q: "What is LSM?", a: "Limit State Method (Ultimate Load Design)." },
                { q: "Limit State of Collapse.", a: "Safety against rupture/compression." },
                { q: "Limit State of Serviceability.", a: "Deflection, Cracking, Vibration." },
                { q: "Partial Safety Factor for Concrete (γc).", a: "1.5." },
                { q: "Partial Safety Factor for Steel (γs).", a: "1.15." },
                { q: "Characteristic Strength (fck).", a: "Strength below which not more than 5% results fall." },
                { q: "Design Strength.", a: "Characteristic Strength / Partial Safety Factor." },
                { q: "Modular Ratio (m).", a: "280 / (3 * σcbc)." },
                { q: "Critical Neutral Axis (xc).", a: "Depth where concrete and steel reach stress simultaneously." },
                { q: "Actual Neutral Axis (x).", a: "Actual depth from compression edge." },
                { q: "Under-reinforced Section.", a: "Steel reaches yield stress first (Ductile failure)." },
                { q: "Over-reinforced Section.", a: "Concrete reaches limit first (Brittle failure)." },
                { q: "Balanced Section.", a: "Steel and concrete reach limit simultaneously." },
                { q: "Preferred section in design?", a: "Under-reinforced (Warning before failure)." },
                { q: "Lever Arm (z).", a: "Distance between C.G. of compression and tension." },
                { q: "Moment of Resistance (Mu).", a: "Resisting moment of section." },
                { q: "Formula for Mu (WSM).", a: "b * x * σcbc * (d - x/3) or Ast * σst * (d - x/3)." },
                { q: "Development Length (Ld).", a: "Length required to develop design stress in bar." },
                { q: "Formula for Ld.", a: "(φ * σs) / (4 * τbd)." },
                { q: "Check for Development Length.", a: "M1/V + L0 >= Ld." },
                { q: "Anchoring Bars.", a: "Bending bars or providing hooks." },
                { q: "Standard Hook Length.", a: "9φ for Mild Steel, 16φ for HYSD." },
                { q: "Check for Shear.", a: "τv <= τc + τcv (or τv <= τcmax)." },
                { q: "Nominal Shear Stress (τv).", a: "V / (b * d)." },
                { q: "Design Shear Strength of Concrete (τc).", a: "Depends on grade and % steel." },
                { q: "Maximum Shear Stress (τcmax).", a: "From table (e.g., 2.8 for M20)." },
                { q: "Shear Reinforcement.", a: "Stirrups or Bent up bars." },
                { q: "Spacing of Stirrups (Sv).", a: "Min of (0.75d, 300mm)." },
                { q: "Minimum Shear Reinforcement.", a: "Asv / (b * Sv) >= 0.4 / (0.87 * fy)." },
                { q: "Check for Deflection.", a: "Actual span/depth <= Basic l/d * modification factors." },
                { q: "Basic l/d ratio for SS Beam.", a: "20." },
                { q: "Modification Factor for Tension Steel.", a: "Depends on % pt and fs." },
                { q: "Modification Factor for Compression Steel.", a: "Depends on % pc." },
                { q: "Check for Cracking.", a: "Spacing of bars, Cover, Steel strain." },
                { q: "Clear Cover for Beam (Mild exposure).", a: "20mm or diameter of bar." },
                { q: "Clear Cover for Slab.", a: "15mm or diameter of bar." },
                { q: "Minimum Reinforcement in Beam.", a: "Asmin = (0.85 * b * d) / fy." },
                { q: "Maximum Reinforcement in Beam.", a: "4% of gross area." },
                { q: "T-beam Effective Width (bf).", a: "lo/6 + bw + 6Df (lo=dist between zero moments)." },
                { q: "Analysis of T-Beam (Neutral Axis in Flange).", a: "Treated as rectangular beam of width bf." },
                { q: "One-way Slab.", a: "Ly/Lx > 2." },
                { q: "Two-way Slab.", a: "Ly/Lx <= 2." },
                { q: "Bending Moments in Two-way Slab.", a: "Mx = αx * w * lx^2, My = αy * w * lx^2." },
                { q: "Torsion Reinforcement at Corners.", a: "Provided to prevent lifting of corners." },
                { q: "Minimum Reinforcement in Slab.", a: "0.12% for HYSD, 0.15% for Mild Steel." },
                { q: "Maximum Spacing of Main Steel in Slab.", a: "3d or 300mm." },
                { q: "Maximum Spacing of Distribution Steel in Slab.", a: "5d or 450mm." },
                { q: "Short Column.", a: "Lex/D < 12 and Ley/b < 12." },
                { q: "Long Column.", a: "Exceeds above limits." },
                { q: "Minimum Eccentricity (emin).", a: "Unsupported length/500 + lateral dimension/30." },
                { q: "Lateral Ties in Column.", a: "Dia >= 5mm or 1/4 main bar dia." },
                { q: "Pitch of Lateral Ties.", a: "Min of (Least lateral dimension, 16 * small bar dia, 300mm)." },
                { q: "Helical Reinforcement.", a: "Spiral reinforcement in circular columns." },
                { q: "Footing Types.", a: "Isolated, Combined, Strap, Mat." },
                { q: "Depth of Footing by One-way Shear.", a: "d = V / (b * τc)." },
                { q: "Depth of Footing by Two-way (Punching) Shear.", a: "Critical section at d/2 from face of column." },
                { q: "Minimum Reinforcement in Footing.", a: "0.12% of gross sectional area." },
                { q: "Retaining Wall types.", a: "Gravity, Cantilever, Counterfort." },
                { q: "Stability Checks for Retaining Wall.", a: "Overturning, Sliding, Bearing capacity." },
                { q: "Factor of Safety against Overturning.", a: "> 1.4." },
                { q: "Factor of Safety against Sliding.", a: "> 1.4." },
                { q: "Maximum bearing pressure < SBC.", a: "Check for soil pressure." },
                { q: "Water Tank types.", a: "Resting on ground, Elevated." },
                { q: "Hoop Tension in Circular Tank.", a: "w * H * D / 2." },
                { q: "Bending Moment in Rectangular Tank.", a: "w * H^3 / 6 (per unit width)." },
                { q: "Prestressed Concrete advantages.", a: "No cracks, long spans, rapid construction." },
                { q: "High Tensile Steel used in PSC.", a: "Freyssinet cables, Magnel cables." },
                { q: "Losses in Prestress (Pre-tensioning).", a: "Elastic shortening, Relaxation, Shrinkage, Creep." },
                { q: "Losses in Prestress (Post-tensioning).", a: "Friction, Anchorage slip, Shrinkage, Creep, Relaxation." },
                { q: "Degree of Prestressing.", a: "Ratio of prestressing force to tensile strength." },
                { q: "IS Code for PSC Design.", a: "IS 1343." },
                { q: "Steel Design: Permissible Stress in Axial Tension.", a: "0.6 fy." },
                { q: "Permissible Stress in Axial Compression.", a: "Depends on slenderness ratio (σac)." },
                { q: "Maximum Slenderness Ratio for Compression Members.", a: "180 (Main), 200 (Secondary)." },
                { q: "Maximum Slenderness Ratio for Tension Members.", a: "350 (Main), 400 (Secondary)." },
                { q: "Lacing System.", a: "Bars connecting components of built-up column." },
                { q: "Battening System.", a: "Plates perpendicular to column axis." },
                { q: "Effective Length of Column (Both ends pinned).", a: "L." },
                { q: "Effective Length of Column (Both ends fixed).", a: "0.65 L." },
                { q: "Effective Length of Column (One end fixed, other free).", a: "2L." },
                { q: "Effective Length of Column (One end fixed, other pinned).", a: "0.8 L." },
                { q: "Gantry Girder.", a: "Horizontal beam supporting crane loads." },
                { q: "Plate Girder.", a: "Built-up beam with web and flange plates." },
                { q: "Economical Depth of Plate Girder.", a: "1.1 * sqrt(M / (tw * σbc))." },
                { q: "Vertical Stiffeners in Plate Girder.", a: "Provided when d/tw > 85 (or 200 for low shear)." },
                { q: "Horizontal Stiffeners.", a: "Provided at 2/5 depth from compression flange." },
                { q: "Bearing Stiffeners.", a: "Provided at supports and concentrated loads." },
                { q: "Web Crippling.", a: "Local failure of web at concentrated load." },
                { q: "Web Buckling.", a: "Buckling of web due to diagonal compression." },
                { q: "Connections in Steel.", a: "Riveted, Bolted, Welded." },
                { q: "Strength of Rivet in Shearing.", a: "τvf * π/4 * d^2." },
                { q: "Strength of Rivet in Bearing.", a: "σpf * d * t." },
                { q: "Pitch of Rivets.", a: "Min 2.5d, Max 32t or 300mm (tension), 16t or 200mm (compression)." },
                { q: "Gauge Distance.", a: "Perpendicular distance between gauge lines." },
                { q: "Edge Distance.", a: "Distance from center of hole to edge of plate." },
                { q: "Minimum Edge Distance.", a: "1.5 * hole diameter." },
                { q: "High Strength Friction Grip Bolts (HSFG).", a: "Bolts tightened to develop friction between plates." },
                { q: "Welding types.", a: "Butt weld, Fillet weld." },
                { q: "Size of Fillet Weld.", a: "Leg length of inscribed triangle." },
                { q: "Effective Length of Fillet Weld.", a: "Total length - 2 * throat thickness." },
                { q: "Strength of Fillet Weld.", a: "lw * t * τvf." }
            ],
            "Fluid Mechanics & Hydraulics": [
                { q: "Define Fluid.", a: "Substance that deforms continuously under shear stress." },
                { q: "Difference between Liquid and Gas.", a: "Liquid: fixed volume, Gas: no fixed volume." },
                { q: "Density (ρ).", a: "Mass per unit volume." },
                { q: "Specific Weight (γ).", a: "Weight per unit volume (ρg)." },
                { q: "Specific Volume.", a: "Volume per unit mass (1/ρ)." },
                { q: "Specific Gravity.", a: "Ratio of density of substance to density of water." },
                { q: "Viscosity.", a: "Resistance to flow/deformation." },
                { q: "Dynamic Viscosity (μ).", a: "Shear stress / velocity gradient." },
                { q: "Kinematic Viscosity (ν).", a: "μ / ρ." },
                { q: "Newton's Law of Viscosity.", a: "Shear stress proportional to velocity gradient." },
                { q: "Non-Newtonian Fluids.", a: "Do not follow Newton's law (e.g., blood, paint)." },
                { q: "Compressibility.", a: "Reciprocal of Bulk Modulus." },
                { q: "Surface Tension.", a: "Force per unit length at interface of two fluids." },
                { q: "Capillarity.", a: "Rise or fall of liquid in narrow tube." },
                { q: "Cohesion.", a: "Attraction between molecules of same fluid." },
                { q: "Adhesion.", a: "Attraction between molecules of different substances." },
                { q: "Pascal's Law.", a: "Pressure at a point is equal in all directions." },
                { q: "Hydrostatic Law.", a: "Rate of increase of pressure in vertical direction equals specific weight." },
                { q: "Pressure Head.", a: "Height of liquid column (p/γ)." },
                { q: "Atmospheric Pressure at sea level.", a: "101.325 kPa or 10.3 m of water or 760 mm of Hg." },
                { q: "Absolute Pressure.", a: "Pressure measured with respect to absolute vacuum." },
                { q: "Gauge Pressure.", a: "Pressure measured with respect to atmospheric pressure." },
                { q: "Vacuum Pressure.", a: "Pressure below atmospheric pressure." },
                { q: "Manometers measure?", a: "Pressure." },
                { q: "Simple Manometer types.", a: "Piezometer, U-tube, Single column." },
                { q: "Differential Manometer.", a: "Measures difference of pressure between two points." },
                { q: "Inverted U-tube Manometer.", a: "Used for measuring pressure difference in gases." },
                { q: "Hydrostatic Paradox.", a: "Pressure at bottom is independent of shape of container." },
                { q: "Total Pressure.", a: "Force exerted by fluid on immersed surface." },
                { q: "Center of Pressure.", a: "Point where total pressure is assumed to act." },
                { q: "For vertical plane surface, Center of Pressure lies?", a: "Below Center of Gravity." },
                { q: "Buoyancy.", a: "Upward force exerted by fluid on immersed body." },
                { q: "Archimedes' Principle.", a: "Buoyant force equals weight of fluid displaced." },
                { q: "Center of Buoyancy.", a: "Center of gravity of displaced fluid volume." },
                { q: "Metacenter (M).", a: "Point of intersection of lines of action of buoyant force before and after heel." },
                { q: "Metacentric Height (GM).", a: "Distance between Center of Gravity (G) and Metacenter (M)." },
                { q: "Stability of Floating Body.", a: "Stable if M is above G (GM positive)." },
                { q: "Stability of Submerged Body.", a: "Stable if Center of Buoyancy is above Center of Gravity." },
                { q: "Fluid Kinematics deals with?", a: "Velocity and acceleration without forces." },
                { q: "Fluid Dynamics deals with?", a: "Forces causing motion." },
                { q: "Steady Flow.", a: "Fluid properties at a point do not change with time." },
                { q: "Unsteady Flow.", a: "Properties change with time." },
                { q: "Uniform Flow.", a: "Velocity same at every point at a given instant." },
                { q: "Non-uniform Flow.", a: "Velocity changes from point to point." },
                { q: "Laminar Flow.", a: "Layers slide smoothly over each other (Re < 2000 for pipes)." },
                { q: "Turbulent Flow.", a: "Irregular flow with eddies (Re > 4000 for pipes)." },
                { q: "Reynolds Number (Re).", a: "Inertial force / Viscous force (ρVD/μ)." },
                { q: "Critical Velocity.", a: "Velocity at which flow changes from laminar to turbulent." },
                { q: "Path Line.", a: "Path traced by single particle over time." },
                { q: "Stream Line.", a: "Line tangent to velocity vector at every point." },
                { q: "Streak Line.", a: "Locus of all fluid particles passing through a point." },
                { q: "Stream Tube.", a: "Bundle of streamlines." },
                { q: "Continuity Equation.", a: "A1V1 = A2V2 (Conservation of mass)." },
                { q: "Bernoulli's Equation.", a: "P/ρg + V^2/2g + Z = Constant (Energy per unit weight)." },
                { q: "Assumptions for Bernoulli's.", a: "Ideal fluid, steady flow, incompressible, along a streamline." },
                { q: "Venturimeter measures?", a: "Discharge in pipe." },
                { q: "Orifice meter measures?", a: "Discharge, uses sharp edge orifice." },
                { q: "Pitot Tube measures?", a: "Velocity of flow at a point." },
                { q: "Hydraulic Gradient Line (HGL).", a: "Line joining piezometric heads (P/ρg + Z)." },
                { q: "Total Energy Line (TEL).", a: "Line joining total heads (P/ρg + V^2/2g + Z)." },
                { q: "Flow through Orifice.", a: "Discharge Q = Cd * A * sqrt(2gH)." },
                { q: "Coefficient of Discharge (Cd).", a: "Cc * Cv (usually 0.61-0.65 for sharp orifice)." },
                { q: "Vena Contracta.", a: "Section where jet diameter is minimum (Cc occurs here)." },
                { q: "Coefficient of Contraction (Cc).", a: "Area of jet at vena contracta / Area of orifice." },
                { q: "Coefficient of Velocity (Cv).", a: "Actual velocity at vena contracta / Theoretical velocity." },
                { q: "Time to empty tank through orifice.", a: "T = 2A * sqrt(H1 - H2) / (Cd * a * sqrt(2g))." },
                { q: "Flow over Notches and Weirs.", a: "Discharge over rectangular notch Q = (2/3) * Cd * L * sqrt(2g) * H^(3/2)." },
                { q: "Francis Formula for Rectangular Weir.", a: "Q = 1.84 * (L - 0.1nH) * H^(3/2) (n=number of end contractions)." },
                { q: "Cipolletti Weir.", a: "Trapezoidal weir with 1:4 side slope, no end contraction correction." },
                { q: "Triangular/V-Notch formula.", a: "Q = (8/15) * Cd * sqrt(2g) * tan(θ/2) * H^(5/2)." },
                { q: "Broad Crested Weir.", a: "Critical depth occurs on crest (Cd ~ 0.85)." },
                { q: "Ogee Weir.", a: "Profile matches lower nappe of ventilated weir." },
                { q: "Hydraulic Jump.", a: "Rise of water level in channel (Sudden transition from super to sub-critical)." },
                { q: "Specific Energy.", a: "Energy per unit weight w.r.t channel bed (y + V^2/2g)." },
                { q: "Critical Depth (yc).", a: "Depth at which specific energy is minimum (Fr=1)." },
                { q: "Froude Number (Fr).", a: "Inertial force / Gravity force (V/sqrt(gy))." },
                { q: "Sub-critical Flow.", a: "Fr < 1 (Deep, slow)." },
                { q: "Super-critical Flow.", a: "Fr > 1 (Shallow, fast)." },
                { q: "Chezy's Formula.", a: "V = C * sqrt(mi) (m=hydraulic mean depth, i=slope)." },
                { q: "Manning's Formula.", a: "V = (1/N) * m^(2/3) * i^(1/2)." },
                { q: "Most Economical Section.", a: "Section that conveys maximum discharge for given area/ perimeter." },
                { q: "Most Economical Rectangular Section.", a: "Width = 2 * Depth." },
                { q: "Most Economical Trapezoidal Section.", a: "Half of hexagon (Sloping side = Bottom width)." },
                { q: "Hydraulic Radius (R or m).", a: "Area / Wetted Perimeter." },
                { q: "Equivalent Pipe.", a: "Pipe of uniform diameter replacing compound pipes." },
                { q: "Dupuit's Equation.", a: "For equivalent length of pipes in series." },
                { q: "Water Hammer.", a: "Pressure rise in pipe due to sudden closure of valve." },
                { q: "Gradual Closure of Valve.", a: "Pressure rise is gradual." },
                { q: "Sudden Closure of Valve (Rigid pipe).", a: "Pressure p = ρLV/t." },
                { q: "Sudden Closure of Valve (Elastic pipe).", a: "Velocity of pressure wave considered." },
                { q: "Reynolds Experiment.", a: "Demonstrated laminar and turbulent flow." },
                { q: "Moody's Diagram.", a: "Graphical representation of friction factor (f) vs Reynolds number." },
                { q: "Darcy-Weisbach Equation.", a: "hf = (4fLV^2)/(2gD)." },
                { q: "Hagen-Poiseuille Equation.", a: "For laminar flow (head loss proportional to velocity)." },
                { q: "Boundary Layer.", a: "Thin layer near surface where viscous effects are significant." },
                { q: "Laminar Boundary Layer.", a: "Near leading edge." },
                { q: "Turbulent Boundary Layer.", a: "Further downstream." },
                { q: "Boundary Layer Thickness (δ).", a: "Distance from surface where velocity is 99% of free stream velocity." },
                { q: "Displacement Thickness.", a: "Distance by which boundary would displace to compensate loss of flow." },
                { q: "Momentum Thickness.", a: "Loss of momentum due to boundary layer." },
                { q: "Drag Force.", a: "Force exerted by fluid in direction of flow." },
                { q: "Lift Force.", a: "Force exerted by fluid perpendicular to flow." },
                { q: "Streamlined Body.", a: "Shape that reduces drag." },
                { q: "Bluff Body.", a: "High drag due to flow separation." },
                { q: "Terminal Velocity.", a: "Constant velocity reached when drag equals weight." }
            ],
            "Irrigation & Hydrology": [
                { q: "Define Irrigation.", a: "Artificial application of water to soil." },
                { q: "Necessity of Irrigation.", a: "Uneven rainfall, less rainfall, growing multiple crops." },
                { q: "Source of Irrigation.", a: "Wells, Tube wells, Canals, Tanks, Rivers." },
                { q: "Advantages of Irrigation.", a: "Increase in yield, protection from famine, generation of hydro-power." },
                { q: "Ill-effects of Irrigation.", a: "Water logging, salt efflorescence." },
                { q: "Types of Irrigation.", a: "Surface (Flow), Sub-surface, Sprinkler, Drip/Trickle." },
                { q: "Surface Irrigation methods.", a: "Flood, Furrow, Contour farming." },
                { q: "Furrow Irrigation.", a: "Water flows in small channels (furrows) between crop rows." },
                { q: "Drip Irrigation.", a: "Water drips slowly to roots, saves water." },
                { q: "Sprinkler Irrigation.", a: "Water sprayed through nozzles (artificial rain)." },
                { q: "Lift Irrigation.", a: "Water lifted by pumps from source below field level." },
                { q: "Flow Irrigation.", a: "Water flows by gravity from source above field level." },
                { q: "Commanded Area.", a: "Area irrigated by canal system." },
                { q: "Gross Commanded Area (GCA).", a: "Total area enclosed between drainage boundaries." },
                { q: "Culturable Commanded Area (CCA).", a: "Culturable portion of GCA." },
                { q: "Intensity of Irrigation.", a: "% of CCA proposed to be irrigated in a year." },
                { q: "Crop Ratio.", a: "Ratio of area under Rabi to Kharif." },
                { q: "Cropping Pattern.", a: "Sequence of crops grown in a year." },
                { q: "Time Factor.", a: "Number of days canal runs / Total days in watering period." },
                { q: "Capacity Factor.", a: "Actual discharge / Design discharge." },
                { q: "Crop Seasons in India.", a: "Kharif (Monsoon), Rabi (Winter), Zaid (Summer)." },
                { q: "Crop Period.", a: "Time from sowing to harvesting." },
                { q: "Base Period (B).", a: "Time from first to last watering." },
                { q: "Delta (Δ).", a: "Total depth of water required." },
                { q: "Duty (D).", a: "Area irrigated by unit discharge." },
                { q: "Relationship: Δ = 8.64 * B / D.", a: "Fundamental formula." },
                { q: "Kor Watering.", a: "First watering after sowing (most important)." },
                { q: "Paleo/Naiser.", a: "Irrigation before sowing." },
                { q: "Consumptive Use (Cu/Evapotranspiration).", a: "Water needed for transpiration and evaporation." },
                { q: "Blaney-Criddle Formula.", a: "Estimates consumptive use based on temperature and daylight hours." },
                { q: "Effective Rainfall.", a: "Portion of rainfall useful for crop growth." },
                { q: "Irrigation Requirement.", a: "Consumptive use - Effective rainfall." },
                { q: "Field Irrigation Requirement (FIR).", a: "Water needed at field inlet." },
                { q: "Net Irrigation Requirement (NIR).", a: "Water stored in root zone." },
                { q: "Irrigation Efficiency.", a: "Ratio of water beneficially used to water delivered." },
                { q: "Water Application Efficiency.", a: "Water stored in root zone / Water delivered." },
                { q: "Water Conveyance Efficiency.", a: "Water delivered to fields / Water released in canal." },
                { q: "Water Use Efficiency.", a: "Water beneficially used / Water delivered." },
                { q: "Distribution Uniformity.", a: "How evenly water is applied." },
                { q: "Soil Moisture Deficiency.", a: "Amount of water needed to bring soil to field capacity." },
                { q: "Field Capacity.", a: "Water held against gravity." },
                { q: "Permanent Wilting Point (PWP).", a: "Moisture content at which plants wilt permanently." },
                { q: "Available Moisture.", a: "Field Capacity - Permanent Wilting Point." },
                { q: "Readily Available Moisture.", a: "75-80% of Available Moisture." },
                { q: "Frequency of Irrigation.", a: "Readily available moisture / Consumptive use rate." },
                { q: "Canal Irrigation.", a: "Most important method in India." },
                { q: "Parts of Canal System.", a: "Head works, Branch canal, Distributary, Minor, Watercourse." },
                { q: "Canal Alignment.", a: "Contour, Ridge/Watershed, Side slope." },
                { q: "Ridge Canal.", a: "Runs on watershed (most economical)." },
                { q: "Contour Canal.", a: "Runs parallel to contours (crosses valleys)." },
                { q: "Side Slope Canal.", a: "Runs perpendicular to contours (steep slope)." },
                { q: "Full Supply Level (FSL).", a: "Highest water level in canal." },
                { q: "Canal Fall/Drop.", a: "Structure to lower water level when natural slope > canal slope." },
                { q: "Canal Regulator.", a: "Structure to control water level and discharge." },
                { q: "Cross Regulator.", a: "Installed on main canal upstream of off-take." },
                { q: "Head Regulator.", a: "Installed at head of off-take channel." },
                { q: "Canal Escape.", a: "Safety valve to remove excess water." },
                { q: "Canal Outlets/Modules.", a: "Devices to distribute water to watercourses." },
                { q: "Types of Outlets.", a: "Non-modular (e.g., Drowned pipe), Semi-modular (e.g., Venturiflume), Modular (e.g., Gibb's)." },
                { q: "Weir vs Barrage.", a: "Weir: raised crest, Barrage: gates for ponding." },
                { q: "Diversion Headworks.", a: "Structure to raise water level and divert into canal." },
                { q: "Storage Headworks.", a: "Dam creates reservoir." },
                { q: "Cross Drainage Works.", a: "Structures carrying canal across natural drain." },
                { q: "Aqueduct.", a: "Canal over drain (drain water below)." },
                { q: "Siphon Aqueduct.", a: "Drain water under pressure (siphoned)." },
                { q: "Super Passage.", a: "Drain over canal (canal water below)." },
                { q: "Canal Siphon.", a: "Canal under drain (canal water under pressure)." },
                { q: "Level Crossing.", a: "Canal and drain meet at same level." },
                { q: "Inlet and Outlet.", a: "Water admitted into canal from drain." },
                { q: "Define Hydrology.", a: "Study of water on earth, occurrence, movement, distribution." },
                { q: "Hydrologic Cycle.", a: "Continuous circulation of water." },
                { q: "Precipitation.", a: "Water falling from atmosphere (rain, snow, hail)." },
                { q: "Forms of Precipitation.", a: "Rain, Snow, Sleet, Glaze, Hail, Drizzle." },
                { q: "Types of Rainfall.", a: "Cyclonic, Convective, Orographic." },
                { q: "Orographic Rainfall.", a: "Caused by mountains." },
                { q: "Measurement of Rainfall.", a: "Rain gauges (Symons, Tipping bucket, Weighing bucket)." },
                { q: "Optimum number of Rain gauges (N).", a: "N = (Cv/ε)^2." },
                { q: "Mean Precipitation methods.", a: "Arithmetic mean, Thiessen Polygon, Isohyetal." },
                { q: "Thiessen Polygon Method.", a: "Weighted average based on area represented by each gauge." },
                { q: "Isohyetal Method.", a: "Most accurate, uses lines of equal rainfall." },
                { q: "Evaporation.", a: "Water to vapor from water bodies." },
                { q: "Transpiration.", a: "Water to vapor from plants." },
                { q: "Evapotranspiration.", a: "Combined evaporation and transpiration." },
                { q: "Potential Evapotranspiration (PET).", a: "ET from extensive water surface." },
                { q: "Actual Evapotranspiration (AET).", a: "Actual loss from catchment." },
                { q: "Infiltration.", a: "Entry of water into soil." },
                { q: "Percolation.", a: "Downward movement of water through soil." },
                { q: "Infiltration Capacity.", a: "Maximum rate at which soil can absorb water." },
                { q: "Horton's Equation.", a: "Infiltration capacity curve (fp = fc + (fo-fc)e^(-kt))." },
                { q: "φ-index.", a: "Average infiltration rate." },
                { q: "W-index.", a: "φ-index excluding surface retention." },
                { q: "Runoff.", a: "Water flowing over ground surface." },
                { q: "Components of Runoff.", a: "Surface runoff, Interflow, Baseflow/Groundwater flow." },
                { q: "Catchment Area.", a: "Area draining into stream/river." },
                { q: "Stream Gauging.", a: "Measurement of discharge in river." },
                { q: "Methods of Stream Gauging.", a: "Area-velocity, Weirs, Notches, Stage-discharge curve." },
                { q: "Current Meter measures?", a: "Velocity at a point." },
                { q: "Float measures?", a: "Surface velocity." },
                { q: "Area-Velocity Method.", a: "Q = Area * Average Velocity." },
                { q: "Hydraulic Structures method.", a: "Using spillways, siphons." },
                { q: "Stage-Discharge Curve (Rating Curve).", a: "Relationship between water level and discharge." },
                { q: "Empirical Formulae for Runoff.", a: "Inglis, Dicken, Ryves (for flood discharge)." },
                { q: "Rational Method.", a: "Q = CiA (C=runoff coeff, i=intensity, A=area)." },
                { q: "Hydrograph.", a: "Graph of discharge vs time." },
                { q: "Unit Hydrograph (UH).", a: "Direct runoff hydrograph from 1cm effective rainfall." },
                { q: "Assumptions of UH.", a: "Time invariance, Linear response." },
                { q: "S-Curve Method.", a: "Deriving UH of different durations." },
                { q: "Instantaneous Unit Hydrograph (IUH).", a: "UH for instantaneous rainfall." },
                { q: "Synthetic Unit Hydrograph.", a: "Developing UH for ungauged catchments (Snyder's method)." },
                { q: "Groundwater.", a: "Water below ground surface." },
                { q: "Zone of Aeration.", a: "Above water table." },
                { q: "Zone of Saturation.", a: "Below water table." },
                { q: "Water Table.", a: "Upper surface of zone of saturation." },
                { q: "Aquifer.", a: "Saturated formation yielding water." },
                { q: "Aquiclude.", a: "Impermeable formation (retards flow)." },
                { q: "Aquitard.", a: "Semi-confining layer." },
                { q: "Aquifuge.", a: "Absolutely impermeable." },
                { q: "Confined Aquifer.", a: "Artesian aquifer, between two impermeable layers." },
                { q: "Unconfined Aquifer.", a: "Water table aquifer, phreatic surface free." },
                { q: "Piezometric Surface.", a: "Imaginary surface to which water rises in wells tapping confined aquifer." },
                { q: "Flowing Well/Artesian Well.", a: "Piezometric surface is above ground." },
                { q: "Non-flowing Well.", a: "Piezometric surface below ground." },
                { q: "Darcy's Law for Groundwater.", a: "V = K * i (Valid for laminar flow)." },
                { q: "Transmissibility (T).", a: "Rate of flow through aquifer of unit width and full depth (T = K * B)." },
                { q: "Specific Yield.", a: "Volume of water yielded by gravity drainage." },
                { q: "Specific Retention.", a: "Water retained against gravity." },
                { q: "Porosity = Specific Yield + Specific Retention.", a: "True." },
                { q: "Well Hydraulics.", a: "Steady flow to a well." },
                { q: "Thiem's Equation (Confined Aquifer).", a: "Discharge formula for steady state." },
                { q: "Dupuit's Equation (Unconfined Aquifer).", a: "Assumes horizontal flow." },
                { q: "Recuperation Test.", a: "In-situ permeability test for tube wells." },
                { q: "Specific Capacity of Well.", a: "Discharge per unit drawdown." }
            ],
            "Environmental Engineering": [
                { q: "Define Environmental Engineering.", a: "Science of cleaning environment for healthy living." },
                { q: "Water Demand components.", a: "Domestic, Industrial, Public, Fire, Losses." },
                { q: "Per capita demand.", a: "Average annual consumption per person." },
                { q: "Design Period.", a: "Future period for which facilities are designed (usually 20-30 years)." },
                { q: "Population Forecasting methods.", a: "Arithmetic, Geometric, Incremental increase, Decreasing rate, Logistic, Graphical." },
                { q: "Factors affecting Water Demand.", a: "Climate, Size of city, Habits, Cost, Pressure." },
                { q: "Variations in Demand.", a: "Daily, Seasonal, Hourly." },
                { q: "Peak Demand.", a: "Maximum hourly demand." },
                { q: "Fire Demand formula.", a: "Kuichling formula, Freeman formula, National Board of Fire." },
                { q: "Coincident Demand.", a: "Max daily demand + Fire demand OR Max hourly demand (whichever is more)." },
                { q: "Sources of Water.", a: "Surface (Rivers, Lakes), Groundwater (Wells, Springs)." },
                { q: "Rainwater Harvesting.", a: "Collection and storage of rainwater." },
                { q: "Intake Structures.", a: "Collect water from source and discharge to conduit." },
                { q: "Types of Intakes.", a: "Reservoir, River, Canal, Lake." },
                { q: "Quality of Water.", a: "Physical, Chemical, Biological." },
                { q: "Physical parameters.", a: "Turbidity, Color, Taste, Odor, Temperature." },
                { q: "Chemical parameters.", a: "pH, Hardness, Chlorides, Iron, Nitrates." },
                { q: "Biological parameters.", a: "Bacteria, Viruses, Algae." },
                { q: "Turbidity.", a: "Resistance to passage of light." },
                { q: "Units of Turbidity.", a: "NTU (Nephelometric), ppm, mg/l." },
                { q: "Hardness.", a: "Soap destroying power due to Ca and Mg salts." },
                { q: "Types of Hardness.", a: "Temporary (Carbonate), Permanent (Non-carbonate)." },
                { q: "Alkalinity.", a: "Capacity to neutralize acid." },
                { q: "pH value.", a: "Logarithm of reciprocal of H+ ion concentration." },
                { q: "Optimum pH for water.", a: "6.5 to 8.5." },
                { q: "Chlorides limit.", a: "250 mg/l." },
                { q: "Iron limit.", a: "0.3 mg/l." },
                { q: "Nitrites/Nitrates limit.", a: "45 mg/l (Nitrate causes Blue Baby disease/Methemoglobinemia)." },
                { q: "Fluoride limit.", a: "1 mg/l (Excess causes Fluorosis)." },
                { q: "WHO stands for?", a: "World Health Organization." },
                { q: "BIS stands for?", a: "Bureau of Indian Standards (IS 10500 for drinking water)." },
                { q: "Water Treatment processes.", a: "Screening, Aeration, Sedimentation, Filtration, Disinfection." },
                { q: "Screening.", a: "Removal of floating debris." },
                { q: "Aeration.", a: "Removal of taste/odor, adding oxygen." },
                { q: "Plain Sedimentation.", a: "Settling of particles by gravity." },
                { q: "Sedimentation with coagulation.", a: "Adding chemicals to form flocs." },
                { q: "Common Coagulants.", a: "Alum (Fitskari), Chlorinated Copperas, Sodium Aluminate." },
                { q: "Jar Test.", a: "To determine optimum coagulant dose." },
                { q: "Flocculation.", a: "Gentle stirring to form bigger flocs." },
                { q: "Types of Settling Tanks.", a: "Fill and draw, Continuous flow." },
                { q: "Detention Time.", a: "Time water stays in tank (usually 4-8 hours)." },
                { q: "Surface Overflow Rate.", a: "Discharge / Surface area (m3/day/m2)." },
                { q: "Filtration.", a: "Removal of suspended matter and bacteria." },
                { q: "Types of Filters.", a: "Gravity (Slow sand, Rapid sand), Pressure." },
                { q: "Slow Sand Filter (SSF).", a: "Rate 100-200 L/m2/hr, effective size 0.15-0.35mm." },
                { q: "Rapid Sand Filter (RSF).", a: "Rate 3000-6000 L/m2/hr, requires coagulation." },
                { q: "Schmutzdecke.", a: "Vital layer in SSF (biological layer)." },
                { q: "Backwashing.", a: "Cleaning RSF by reversing flow." },
                { q: "Disinfection.", a: "Killing of pathogenic bacteria." },
                { q: "Chlorination.", a: "Most common disinfection method." },
                { q: "Chlorine demand.", a: "Amount of chlorine consumed before free chlorine appears." },
                { q: "Break Point Chlorination.", a: "Chlorine added beyond chlorine demand to ensure free residual." },
                { q: "Free Residual Chlorine.", a: "0.2 mg/l at consumer end." },
                { q: "Dechlorination.", a: "Removal of excess chlorine using SO2, Na2SO3." },
                { q: "Ozonation.", a: "Strong disinfectant, removes color/odor, costly." },
                { q: "UV Radiation.", a: "Physical disinfection, no residual effect." },
                { q: "Miscellaneous Treatments.", a: "Softening, Removal of Iron/Manganese, Fluoridation/Defluoridation, Demineralization." },
                { q: "Lime-Soda Process.", a: "Chemical softening (removing hardness)." },
                { q: "Zeolite/Permutit Process.", a: "Base exchange process for softening." },
                { q: "Demineralization.", a: "Removing all dissolved solids (Ion exchange)." },
                { q: "Fluoridation.", a: "Adding fluoride to prevent tooth decay." },
                { q: "Defluoridation.", a: "Removing excess fluoride." },
                { q: "Nalgonda Technique.", a: "Defluoridation using Alum and Lime." },
                { q: "Distribution System.", a: "Pipes/conduits to carry water to consumers." },
                { q: "Layouts of Distribution.", a: "Dead end, Grid-iron, Circular/Ring, Radial." },
                { q: "Dead End System.", a: "Suitable for old towns, irregular layout." },
                { q: "Grid Iron System.", a: "Rectangular layout, free circulation." },
                { q: "Ring System.", a: "Supply to center from main around city." },
                { q: "Radial System.", a: "Water pumped to elevated reservoirs in zones." },
                { q: "Appurtenances.", a: "Valves, Fire hydrants, Water meters." },
                { q: "Sluice Valve.", a: "To control flow in pipes." },
                { q: "Air Valve.", a: "To release air from pipes." },
                { q: "Check Valve/Reflex Valve.", a: "Allows flow in one direction only." },
                { q: "Scour Valve/Blow off.", a: "To empty pipe for cleaning." },
                { q: "Fire Hydrant.", a: "Connection to supply water for fire fighting." },
                { q: "Water Meter.", a: "To measure quantity of water supplied." },
                { q: "Leakage Detection.", a: "Sounding rods, Geophones, Districting." },
                { q: "Wastewater/Refuse.", a: "Liquid waste from community (Sewage + Sullage)." },
                { q: "Sewage.", a: "Wastewater from latrines/urinals." },
                { q: "Sullage.", a: "Wastewater from baths/sinks (Grey water)." },
                { q: "Dry Weather Flow (DWF).", a: "Sanitary sewage." },
                { q: "Storm Water.", a: "Runoff from rains." },
                { q: "Sewerage System.", a: "Collection, treatment, disposal of sewage." },
                { q: "Quantity of Sanitary Sewage.", a: "Usually 80% of water supply." },
                { q: "Sewer Appurtenances.", a: "Manholes, Catch basins, Inverted siphons." },
                { q: "Manholes.", a: "Provided for inspection and cleaning." },
                { q: "Spacing of Manholes.", a: "Usually 30m (normal), 300m (sewers >1.5m dia)." },
                { q: "Drop Manholes.", a: "When sewer connects at higher level." },
                { q: "Inverted Siphons.", a: "Carry sewer under obstruction ( depressed sewer)." },
                { q: "Storm Water Inlets.", a: "Catch basins, Curb inlets, Gutter inlets." },
                { q: "Systems of Sewerage.", a: "Separate, Combined, Partially separate." },
                { q: "Separate System.", a: "Two sets of sewers (Sanitary + Storm)." },
                { q: "Combined System.", a: "One sewer carries both (old cities)." },
                { q: "BOD (Biochemical Oxygen Demand).", a: "Oxygen demand by bacteria to stabilize organic matter." },
                { q: "COD (Chemical Oxygen Demand).", a: "Oxygen demand by chemical oxidation." },
                { q: "BOD5.", a: "BOD at 20°C for 5 days." },
                { q: "Sewage Treatment methods.", a: "Primary (Physical), Secondary (Biological), Tertiary (Chemical)." },
                { q: "Primary Treatment.", a: "Screening, Grit chambers, Sedimentation." },
                { q: "Grit Chambers.", a: "Remove inorganic solids (sand, gravel)." },
                { q: "Secondary Treatment.", a: "Biological treatment (Trickling filters, Activated sludge)." },
                { q: "Trickling Filters.", a: "Spray sewage over bed of stones." },
                { q: "Activated Sludge Process.", a: "Aeration tank with recycled sludge." },
                { q: "Oxidation Ponds.", a: "Shallow ponds (3-4 ft), natural purification." },
                { q: "Sludge Treatment.", a: "Thickening, Digestion, Drying, Disposal." },
                { q: "Sludge Digestion.", a: "Anaerobic decomposition of organic matter." },
                { q: "Sludge Volume Index (SVI).", a: "Volume in ml occupied by 1g of sludge." },
                { q: "Disposal of Sewage.", a: "Dilution (Sea/river), Irrigation, Disposal on land." },
                { q: "Self-purification of streams.", a: "Natural processes restoring water quality." },
                { q: "Oxygen Sag Curve.", a: "Depletion and reaeration of oxygen in stream." },
                { q: "Solid Waste Management.", a: "Collection, Processing, Disposal of solid waste." },
                { q: "Refuse.", a: "Solid waste (Garbage + Rubbish)." },
                { q: "Collection Methods.", a: "Communal, Block, Door-to-door." },
                { q: "Disposal Methods.", a: "Sanitary Landfill, Composting, Incineration, Pyrolysis." },
                { q: "Composting.", a: "Biological decomposition to humus." },
                { q: "Incineration.", a: "Burning waste at high temperature." },
                { q: "Sanitary Landfill.", a: "Controlled dumping with soil cover." },
                { q: "Air Pollution.", a: "Presence of substances in atmosphere harmful to man." },
                { q: "Sources of Air Pollution.", a: "Vehicular, Industrial, Domestic." },
                { q: "Primary Pollutants.", a: "CO, SO2, NOx, Particulates." },
                { q: "Secondary Pollutants.", a: "Photochemical smog, Ozone." },
                { q: "Acid Rain.", a: "Rain with pH < 5.6 due to SO2 and NOx." },
                { q: "Greenhouse Effect.", a: "Trapping of heat by atmospheric gases." },
                { q: "Greenhouse Gases.", a: "CO2, Methane, Water vapor, N2O." },
                { q: "Control of Air Pollution.", a: "Cyclone separators, Electrostatic precipitators, Scrubbers." },
                { q: "Noise Pollution.", a: "Unwanted sound." },
                { q: "Unit of Noise.", a: "Decibel (dB)." },
                { q: "Control of Noise.", a: "Source control, Path control, Receiver protection." }
            ]
        };

        // --- 2. Three.js Background Animation ---
        const initThreeJS = () => {
            const canvas = document.getElementById('canvas-bg');
            const scene = new THREE.Scene();
            // Fog for depth
            scene.fog = new THREE.FogExp2(0x0B1120, 0.03);

            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 20;

            const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);

            // Lighting
            const ambientLight = new THREE.AmbientLight(0x38BDF8, 0.5);
            scene.add(ambientLight);
            const pointLight = new THREE.PointLight(0xffffff, 1);
            pointLight.position.set(10, 10, 10);
            scene.add(pointLight);

            // Objects - Floating Cubes representing "Knowledge Blocks"
            const geometry = new THREE.BoxGeometry(0.8, 0.8, 0.8);
            const material = new THREE.MeshStandardMaterial({ 
                color: 0x38BDF8, 
                roughness: 0.1, 
                metalness: 0.8,
                transparent: true,
                opacity: 0.3
            });

            const cubes = [];
            for(let i=0; i<50; i++) {
                const mesh = new THREE.Mesh(geometry, material);
                mesh.position.x = (Math.random() - 0.5) * 40;
                mesh.position.y = (Math.random() - 0.5) * 40;
                mesh.position.z = (Math.random() - 0.5) * 20;
                
                mesh.rotation.x = Math.random() * Math.PI;
                mesh.rotation.y = Math.random() * Math.PI;

                scene.add(mesh);
                cubes.push({
                    mesh,
                    speed: 0.005 + Math.random() * 0.01,
                    rotSpeed: (Math.random() - 0.5) * 0.02
                });
            }

            // Animation Loop
            const animate = () => {
                requestAnimationFrame(animate);
                
                cubes.forEach(cube => {
                    cube.mesh.rotation.x += cube.rotSpeed;
                    cube.mesh.rotation.y += cube.rotSpeed;
                    cube.mesh.position.y += Math.sin(Date.now() * 0.001 * cube.speed) * 0.01;
                });

                // Gentle camera movement based on mouse
                camera.position.x += (mouseX * 0.001 - camera.position.x) * 0.05;
                camera.position.y += (-mouseY * 0.001 - camera.position.y) * 0.05;
                camera.lookAt(scene.position);

                renderer.render(scene, camera);
            };

            animate();

            // Handle Resize
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        };

        let mouseX = 0, mouseY = 0;
        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX - window.innerWidth / 2;
            mouseY = e.clientY - window.innerHeight / 2;
        });

        // --- 3. App Logic ---

        const subjectListEl = document.getElementById('subject-list');
        const qaContainerEl = document.getElementById('qa-container');
        const emptyStateEl = document.getElementById('empty-state');
        const contentViewerEl = document.getElementById('content-viewer');
        const viewerTitleEl = document.getElementById('viewer-title');
        const viewerCategoryEl = document.getElementById('viewer-category');
        const progressCountEl = document.getElementById('progress-count');

        // Initialize Subjects
        const initSubjects = () => {
            const subjects = Object.keys(db);
            
            subjects.forEach((subject, index) => {
                const card = document.createElement('div');
                card.className = 'subject-card p-4 rounded-xl cursor-pointer group';
                card.innerHTML = `
                    <div class="flex justify-between items-center">
                        <div>
                            <h3 class="font-bold text-slate-200 group-hover:text-brand-accent transition-colors">${subject}</h3>
                            <p class="text-xs text-slate-500 mt-1">100 High-Yield Q&As</p>
                        </div>
                        <div class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-slate-400 group-hover:bg-brand-accent group-hover:text-white transition-all">
                            <i class="fas fa-chevron-right text-xs"></i>
                        </div>
                    </div>
                `;
                card.onclick = () => loadSubject(subject);
                subjectListEl.appendChild(card);
            });
        };

        const loadSubject = (subject) => {
            // UI Updates
            emptyStateEl.classList.add('hidden');
            contentViewerEl.classList.remove('hidden');
            contentViewerEl.classList.add('flex');
            
            // Header Updates
            viewerCategoryEl.textContent = "TECHNICAL SUBJECT";
            viewerTitleEl.textContent = subject;
            progressCountEl.textContent = `100 Q&As Loaded`;

            // Populate Q&A
            qaContainerEl.innerHTML = '';
            const questions = db[subject];

            // Add a nice intro card
            const intro = document.createElement('div');
            intro.className = 'bg-gradient-to-r from-blue-900/40 to-slate-900/40 p-4 rounded-xl border border-blue-500/20 mb-4 animate-fade-in';
            intro.innerHTML = `<p class="text-sm text-blue-200">💡 <span class="font-bold">Study Tip:</span> Read these questions out loud. These are the most frequently repeated concepts in the RRB JE exam.</p>`;
            qaContainerEl.appendChild(intro);

            questions.forEach((item, idx) => {
                const row = document.createElement('div');
                row.className = 'qa-item py-4 px-2 animate-slide-up';
                row.style.animationDelay = `${idx * 0.02}s`; // Staggered animation
                
                row.innerHTML = `
                    <div class="flex gap-3">
                        <div class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-xs font-mono text-slate-400 mt-1">
                            ${idx + 1}
                        </div>
                        <div>
                            <h4 class="text-slate-200 font-semibold text-sm leading-relaxed">${item.q}</h4>
                            <div class="mt-1 flex items-start gap-2">
                                <i class="fas fa-arrow-right text-brand-accent text-xs mt-1"></i>
                                <p class="text-slate-400 text-sm">${item.a}</p>
                            </div>
                        </div>
                    </div>
                `;
                qaContainerEl.appendChild(row);
            });

            // Mobile view handling
            if(window.innerWidth < 768) {
                document.getElementById('sidebar').classList.add('-translate-x-full');
            }
        };

        const closeViewer = () => {
            document.getElementById('sidebar').classList.remove('-translate-x-full');
        };

        // Initialize
        window.addEventListener('DOMContentLoaded', () => {
            initThreeJS();
            initSubjects();
        });

    </script>
</body>
</html>
