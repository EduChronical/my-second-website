<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RRB JE 2026 Civil Prep | AI Mentor</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Orbitron:wght@500;700;900&display=swap');

        body {
            margin: 0;
            overflow: hidden;
            font-family: 'Inter', sans-serif;
            background-color: #0f172a;
        }

        #canvas-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
        }

        .ui-layer {
            position: relative;
            z-index: 10;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .glass-panel {
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }

        .title-font {
            font-family: 'Orbitron', sans-serif;
        }

        .chat-bubble {
            max-width: 80%;
            padding: 12px 18px;
            border-radius: 20px;
            margin-bottom: 12px;
            position: relative;
            animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            word-wrap: break-word;
        }

        @keyframes popIn {
            from { opacity: 0; transform: translateY(10px) scale(0.9); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        .bot-msg {
            background: rgba(59, 130, 246, 0.2);
            border: 1px solid rgba(59, 130, 246, 0.3);
            color: #e2e8f0;
            border-bottom-left-radius: 4px;
            align-self: flex-start;
        }

        .user-msg {
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            color: white;
            border-bottom-right-radius: 4px;
            align-self: flex-end;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.05); 
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(59, 130, 246, 0.5); 
            border-radius: 10px;
        }

        .option-btn {
            transition: all 0.2s ease;
        }
        .option-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
        }
        
        .typing-indicator span {
            display: inline-block;
            width: 6px;
            height: 6px;
            background-color: #93c5fd;
            border-radius: 50%;
            animation: typing 1.4s infinite ease-in-out both;
            margin: 0 2px;
        }
        
        .typing-indicator span:nth-child(1) { animation-delay: -0.32s; }
        .typing-indicator span:nth-child(2) { animation-delay: -0.16s; }
        
        @keyframes typing {
            0%, 80%, 100% { transform: scale(0); }
            40% { transform: scale(1); }
        }
    </style>
</head>
<body>

    <!-- 3D Background Canvas -->
    <div id="canvas-container"></div>

    <!-- Main UI Container -->
    <div class="ui-layer p-4">
        
        <!-- Header -->
        <div class="absolute top-0 left-0 w-full p-6 flex justify-between items-center pointer-events-none">
            <div class="pointer-events-auto flex items-center gap-3">
                <div class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center shadow-lg shadow-blue-500/50">
                    <i class="fas fa-train text-white text-xl"></i>
                </div>
                <div>
                    <h1 class="text-white font-bold text-lg tracking-wide title-font">RRB JE <span class="text-blue-400">2026</span></h1>
                    <p class="text-slate-400 text-xs uppercase tracking-widest">Civil Engineering Prep</p>
                </div>
            </div>
            <div class="pointer-events-auto hidden md:block">
                <span class="px-3 py-1 rounded-full border border-blue-500/30 text-blue-400 text-xs font-semibold bg-blue-500/10">
                    <i class="fas fa-circle text-[8px] mr-2 animate-pulse"></i>Live AI Mentor
                </span>
            </div>
        </div>

        <!-- Chat Interface -->
        <div class="glass-panel w-full max-w-md h-[600px] rounded-3xl flex flex-col overflow-hidden relative transition-all duration-500">
            
            <!-- Chat Header -->
            <div class="p-4 border-b border-white/10 bg-slate-900/50 flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div class="relative">
                        <img src="https://ui-avatars.com/api/?name=AI+Mentor&background=2563eb&color=fff" class="w-10 h-10 rounded-full border-2 border-blue-500">
                        <div class="absolute bottom-0 right-0 w-3 h-3 bg-green-500 border-2 border-slate-900 rounded-full"></div>
                    </div>
                    <div>
                        <h3 class="text-white font-semibold text-sm">Civil Prep Bot</h3>
                        <p class="text-slate-400 text-xs">Online & Ready</p>
                    </div>
                </div>
                <button onclick="resetChat()" class="text-slate-400 hover:text-white transition-colors" title="Restart Chat">
                    <i class="fas fa-redo-alt"></i>
                </button>
            </div>

            <!-- Messages Area -->
            <div id="chat-messages" class="flex-1 overflow-y-auto p-4 flex flex-col bg-slate-900/30">
                <!-- Initial Message will be injected by JS -->
            </div>

            <!-- Input Area -->
            <div class="p-4 border-t border-white/10 bg-slate-900/80 backdrop-blur-md">
                <div id="user-options" class="grid grid-cols-1 gap-2 mb-3">
                    <!-- Dynamic Buttons -->
                </div>
                <div class="relative hidden" id="text-input-area">
                    <input type="text" id="user-input" placeholder="Type a subject..." 
                           class="w-full bg-slate-800 text-white text-sm rounded-full pl-4 pr-12 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 border border-slate-700">
                    <button onclick="sendMessage()" class="absolute right-2 top-1/2 transform -translate-y-1/2 w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white hover:bg-blue-500 transition-colors">
                        <i class="fas fa-paper-plane text-xs"></i>
                    </button>
                </div>
            </div>
        </div>

        <div class="absolute bottom-6 text-slate-500 text-xs text-center w-full pointer-events-none">
            Designed for RRB JE 2026 Aspirants • Educational Purpose Only
        </div>
    </div>

    <script>
        // --- 1. Three.js 3D Background Animation ---
        const init3D = () => {
            const container = document.getElementById('canvas-container');
            const scene = new THREE.Scene();
            
            // Fog for depth
            scene.fog = new THREE.FogExp2(0x0f172a, 0.02);

            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 30;

            const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            container.appendChild(renderer.domElement);

            // Create particles (Stars/Dust)
            const particlesGeometry = new THREE.BufferGeometry();
            const particlesCount = 1000;
            const posArray = new Float32Array(particlesCount * 3);

            for(let i = 0; i < particlesCount * 3; i++) {
                posArray[i] = (Math.random() - 0.5) * 100;
            }

            particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
            const particlesMaterial = new THREE.PointsMaterial({
                size: 0.15,
                color: 0x60a5fa,
                transparent: true,
                opacity: 0.8,
                blending: THREE.AdditiveBlending
            });
            const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
            scene.add(particlesMesh);

            // Create Geometric Shapes representing Engineering/Civil
            const geometries = [
                new THREE.IcosahedronGeometry(1, 0),
                new THREE.BoxGeometry(1, 1, 1),
                new THREE.TetrahedronGeometry(1),
                new THREE.OctahedronGeometry(1)
            ];

            const objects = [];
            const material = new THREE.MeshStandardMaterial({
                color: 0x2563eb,
                wireframe: true,
                emissive: 0x1e40af,
                emissiveIntensity: 0.2
            });

            for (let i = 0; i < 15; i++) {
                const geom = geometries[Math.floor(Math.random() * geometries.length)];
                const mesh = new THREE.Mesh(geom, material);
                
                mesh.position.x = (Math.random() - 0.5) * 40;
                mesh.position.y = (Math.random() - 0.5) * 40;
                mesh.position.z = (Math.random() - 0.5) * 20;
                
                mesh.rotation.x = Math.random() * Math.PI;
                mesh.rotation.y = Math.random() * Math.PI;
                
                const scale = Math.random() * 2 + 0.5;
                mesh.scale.set(scale, scale, scale);

                scene.add(mesh);
                objects.push({
                    mesh: mesh,
                    rotSpeedX: (Math.random() - 0.5) * 0.01,
                    rotSpeedY: (Math.random() - 0.5) * 0.01,
                    floatSpeed: Math.random() * 0.02,
                    floatOffset: Math.random() * Math.PI * 2
                });
            }

            // Lighting
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
            scene.add(ambientLight);
            const pointLight = new THREE.PointLight(0x3b82f6, 2);
            pointLight.position.set(10, 10, 10);
            scene.add(pointLight);

            // Animation Loop
            const clock = new THREE.Clock();

            const animate = () => {
                const elapsedTime = clock.getElapsedTime();
                
                // Rotate entire particle system slowly
                particlesMesh.rotation.y = elapsedTime * 0.05;

                // Animate individual objects
                objects.forEach(obj => {
                    obj.mesh.rotation.x += obj.rotSpeedX;
                    obj.mesh.rotation.y += obj.rotSpeedY;
                    
                    // Floating effect
                    obj.mesh.position.y += Math.sin(elapsedTime + obj.floatOffset) * 0.01;
                });

                // Mouse interaction (subtle parallax)
                camera.position.x += (mouseX * 0.05 - camera.position.x) * 0.05;
                camera.position.y += (-mouseY * 0.05 - camera.position.y) * 0.05;
                camera.lookAt(scene.position);

                renderer.render(scene, camera);
                requestAnimationFrame(animate);
            };

            animate();

            // Handle Resize
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        };

        let mouseX = 0;
        let mouseY = 0;
        document.addEventListener('mousemove', (event) => {
            mouseX = (event.clientX - window.innerWidth / 2);
            mouseY = (event.clientY - window.innerHeight / 2);
        });

        // --- 2. Chatbot Logic & Data ---

        // RRB JE 2026 Civil Syllabus Data (Condensed)
        const syllabusData = {
            "General Awareness": [
                "Current affairs (National & International)",
                "Indian Geography",
                "Culture and History of India",
                "Indian Economy",
                "Indian Polity",
                "Environmental issues concerning India",
                "General Scientific and Technological developments"
            ],
            "Arithmetic": [
                "Number systems",
                "BODMAS, Decimals & Fractions",
                "LCM and HCF",
                "Ratio and Proportion",
                "Percentages, Mensuration",
                "Time and Work, Time and Distance",
                "Simple and Compound Interest",
                "Profit and Loss, Algebra, Geometry"
            ],
            "General Intelligence & Reasoning": [
                "Analogies, Alphabetical and Number Series",
                "Coding and Decoding, Mathematical operations",
                "Relationships, Syllogism",
                "Jumbling, Venn Diagram",
                "Data Interpretation and Sufficiency",
                "Conclusions and Decision Making",
                "Similarities and Differences",
                "Analytical Reasoning, Classification"
            ],
            "General Science": [
                "Physics (Up to 10th standard CBSE)",
                "Chemistry (Up to 10th standard CBSE)",
                "Life Sciences (Up to 10th standard CBSE)"
            ],
            "Technical: Civil Engineering": [
                "Engineering Mechanics",
                "Building Construction & Materials",
                "Concrete Technology",
                "Surveying",
                "Soil Mechanics & Foundation Engineering",
                "Hydraulics & Fluid Mechanics",
                "Irrigation Engineering",
                "Transportation Engineering",
                "Estimating & Costing",
                "Structural Analysis",
                "Steel & R.C.C Design",
                "Environmental Engineering",
                "Construction Management",
                "Computer Aided Design (CAD)"
            ]
        };

        // Q&A Data (Sample 50 one-liners distributed across topics)
        const questionsData = {
            "Engineering Mechanics": [
                { q: "Define Force.", a: "Force is an agent that produces or tends to produce, destroys or tends to destroy motion." },
                { q: "What is the S.I unit of Force?", a: "Newton (N)." },
                { q: "State Newton's Second Law.", a: "Force is directly proportional to the rate of change of momentum." },
                { q: "What is a Couple?", a: "Two equal and opposite parallel forces acting at different points on a body." },
                { q: "Define Center of Gravity.", a: "The point through which the whole weight of the body acts." },
                { q: "What is the Moment of Inertia?", a: "The second moment of area or mass about an axis." },
                { q: "Define Friction.", a: "The force resisting the relative motion of solid surfaces." },
                { q: "What is Lami's Theorem?", a: "If three coplanar forces acting at a point are in equilibrium, each force is proportional to the sine of the angle between the other two." }
            ],
            "Building Materials": [
                { q: "What is the normal consistency of cement?", a: "The percentage of water required to prepare a paste of standard consistency." },
                { q: "What is Slump Test used for?", a: "To determine the workability of fresh concrete." },
                { q: "Define Curing of Concrete.", a: "Process of maintaining satisfactory moisture content and temperature in freshly cast concrete." },
                { q: "What is the main constituent of cement?", a: "Lime (CaO)." },
                { q: "What is Seasoning of Timber?", a: "Process of drying timber to remove excess moisture." }
            ],
            "Soil Mechanics": [
                { q: "Define Void Ratio.", a: "Ratio of volume of voids to the volume of solids." },
                { q: "What is the Plastic Limit?", a: "The water content at which soil changes from plastic state to semi-solid state." },
                { q: "Define Permeability.", a: "The property of soil which allows water to pass through it." },
                { q: "What is Boussinesq's Theory used for?", a: "Stress distribution in soil due to a point load." },
                { q: "What is Darcy's Law?", a: "v = ki (Velocity of flow is proportional to hydraulic gradient)." }
            ],
            "Structural Analysis": [
                { q: "What is a Statically Determinate Structure?", a: "Conditions of equilibrium are sufficient to analyze it (e.g., Simply supported beam)." },
                { q: "Define Bending Moment.", a: "The algebraic sum of moments about a section of all forces acting on one side of the section." },
                { q: "What is the Point of Contraflexure?", a: "The point where the Bending Moment changes sign (from +ve to -ve)." },
                { q: "State Maxwell's Reciprocal Theorem.", a: "The deflection at A due to unit load at B is equal to deflection at B due to unit load at A." }
            ],
            "RCC Design": [
                { q: "What is the modular ratio (m)?", a: "m = 280/(3*sigma_cbc). Ratio of modulus of elasticity of steel to concrete." },
                { q: "What is development length?", a: "Length of embedded reinforcement required to develop the design stress at the critical section." },
                { q: "Define Limit State Method.", a: "Design method based on safety at ultimate loads and serviceability at working loads." },
                { q: "What is the cover to reinforcement?", a: "Clear distance between the surface of the concrete and the outermost face of the steel bar." }
            ],
            "Transportation": [
                { q: "What is Camber?", a: "The cross slope provided to raise the middle of the road surface in the transverse direction to drain off rainwater." },
                { q: "What is the Super-elevation?", a: "Lateral inclination of the road/rail surface to counteract centrifugal force on curves." },
                { q: "What is CBR?", a: "California Bearing Ratio, a penetration test for evaluating mechanical strength of road subgrades." },
                { q: "Define Gradient.", a: "Rate of rise or fall of road/railway line along its length." }
            ],
            "Irrigation": [
                { q: "What is Delta (Δ)?", a: "Total depth of water required by a crop during its base period." },
                { q: "Define Duty of Water.", a: "Area of land irrigated by unit discharge of water." },
                { q: "What is a Weir?", a: "A barrier across a river to alter its flow characteristics." }
            ],
            "Environmental": [
                { q: "What is BOD?", a: "Biochemical Oxygen Demand - amount of oxygen consumed by bacteria in decomposing organic matter." },
                { q: "What is the pH of drinking water?", a: "Ideally between 6.5 and 8.5." },
                { q: "Define Detention Time.", a: "The theoretical time required for water to pass through a tank at a given flow rate." }
            ]
        };

        // State Management
        let currentState = 'initial'; // initial, waiting_for_topic, showing_qa

        const chatMessages = document.getElementById('chat-messages');
        const userOptions = document.getElementById('user-options');

        // Helper: Add message to chat
        function addMessage(text, sender) {
            const div = document.createElement('div');
            div.className = `chat-bubble ${sender === 'bot' ? 'bot-msg' : 'user-msg'}`;
            div.innerHTML = text;
            chatMessages.appendChild(div);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        // Helper: Show Typing Indicator
        function showTyping() {
            const div = document.createElement('div');
            div.id = 'typing-indicator';
            div.className = 'chat-bubble bot-msg flex gap-1 items-center h-10';
            div.innerHTML = '<div class="typing-indicator"><span></span><span></span><span></span></div>';
            chatMessages.appendChild(div);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function removeTyping() {
            const el = document.getElementById('typing-indicator');
            if(el) el.remove();
        }

        // Helper: Clear Options
        function clearOptions() {
            userOptions.innerHTML = '';
        }

        // Helper: Create Button
        function createButton(text, onClick) {
            const btn = document.createElement('button');
            btn.className = 'option-btn w-full text-left bg-slate-800 hover:bg-blue-600 text-slate-300 hover:text-white p-3 rounded-xl text-sm border border-slate-700 transition-all flex items-center justify-between group';
            btn.innerHTML = `<span>${text}</span> <i class="fas fa-chevron-right opacity-0 group-hover:opacity-100 transition-opacity text-xs"></i>`;
            btn.onclick = onClick;
            userOptions.appendChild(btn);
        }

        // --- Flow Logic ---

        function startChat() {
            clearOptions();
            addMessage("Namaste! 🙏 <br>I'm your RRB JE 2026 <b>Civil Engineering</b> Mentor.", 'bot');
            
            setTimeout(() => {
                addMessage("How can I assist you today?", 'bot');
                createButton("📋 Exam Syllabus & Pattern", () => selectOption('syllabus'));
                createButton("🧠 50 One-Liners (Q&A)", () => selectOption('oneline'));
            }, 600);
        }

        function selectOption(option) {
            // User Click Visuals
            const text = option === 'syllabus' ? "Show Syllabus & Pattern" : "Show One-Liners Q&A";
            addMessage(text, 'user');
            clearOptions();
            showTyping();

            setTimeout(() => {
                removeTyping();
                if (option === 'syllabus') {
                    showSyllabus();
                } else if (option === 'oneline') {
                    showTopicSelection();
                }
            }, 1000);
        }

        function showSyllabus() {
            addMessage("📚 <b>RRB JE 2026 Syllabus Overview</b><br><br>The exam consists of 4 main sections:", 'bot');
            
            let content = "<div class='space-y-2 mt-2'>";
            for (const [category, topics] of Object.entries(syllabusData)) {
                content += `<div class='bg-slate-800/50 p-2 rounded border-l-2 border-blue-500'>
                    <div class='font-bold text-blue-300 text-xs mb-1'>${category}</div>
                    <div class='text-xs text-slate-300'>${topics.slice(0, 2).join(', ')}...</div>
                </div>`;
            }
            content += "</div>";
            content += "<div class='mt-3 text-xs text-slate-400 italic'>Note: Technical section carries the most weight.</div>";
            
            addMessage(content, 'bot');
            
            setTimeout(() => {
                addMessage("Would you like to see the Q&A section now?", 'bot');
                createButton("Yes, Show Q&A Topics", () => selectOption('oneline'));
                createButton("🔁 Start Over", resetChat);
            }, 500);
        }

        function showTopicSelection() {
            addMessage("Great choice! 🎯 Select a Technical Topic to get 5 key one-liners:", 'bot');
            
            const topics = Object.keys(questionsData);
            topics.forEach(topic => {
                createButton(`📐 ${topic}`, () => loadQuestions(topic));
            });
            createButton("🔁 Go Back", resetChat);
        }

        function loadQuestions(topic) {
            addMessage(`Loading <b>${topic}</b>...`, 'user');
            clearOptions();
            showTyping();

            setTimeout(() => {
                removeTyping();
                const questions = questionsData[topic];
                let html = `<div class='text-blue-300 font-bold mb-2 border-b border-white/10 pb-1'>${topic}</div>`;
                
                questions.forEach((item, index) => {
                    html += `
                        <div class='mb-3'>
                            <div class='text-white font-semibold text-sm'>Q${index+1}: ${item.q}</div>
                            <div class='text-blue-200 text-xs mt-1 bg-blue-900/30 p-2 rounded'>A: ${item.a}</div>
                        </div>
                    `;
                });

                addMessage(html, 'bot');
                
                // Add option to continue
                setTimeout(() => {
                    addMessage("Want to practice another topic?", 'bot');
                    createButton("Select Another Topic", showTopicSelection);
                    createButton("🏠 Home", resetChat);
                }, 500);

            }, 1500);
        }

        function resetChat() {
            chatMessages.innerHTML = '';
            startChat();
        }

        // Initialize
        window.onload = () => {
            init3D();
            startChat();
        };

    </script>
</body>
</html>
