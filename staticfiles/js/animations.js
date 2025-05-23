// animations.js - Place in your static/js folder

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate on Scroll)
    AOS.init({
        duration: 800,
        easing: 'ease',
        once: false,
        mirror: false
    });

    // Page Load Animation
    document.body.classList.add('fade-in');
    
    // Counter Animation
    const counters = document.querySelectorAll('.counter-animation');
    
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const duration = 2000; // 2 seconds
        const startTime = Date.now();
        
        function updateCounter() {
            const currentTime = Date.now();
            const elapsedTime = currentTime - startTime;
            const progress = Math.min(elapsedTime / duration, 1);
            
            // Use easeOutQuad easing function for smoother animation
            const easeProgress = 1 - (1 - progress) * (1 - progress);
            const currentValue = Math.floor(easeProgress * target);
            
            counter.innerText = currentValue;
            
            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                counter.innerText = target;
            }
        }
        
        // Start the animation when element is in viewport
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    updateCounter();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        observer.observe(counter);
    });
    
    // Add parallax effect to hero section
    const heroSection = document.querySelector('.hero-section');
    
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrollPosition = window.pageYOffset;
            // Move the background slightly as user scrolls
            heroSection.style.backgroundPositionY = 50 + (scrollPosition * 0.05) + '%';
        });
    }
    
    // Add smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href !== '#') {
                e.preventDefault();
                
                document.querySelector(href).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Initialize AOS animations
    AOS.init({
        duration: 800,
        easing: 'ease',
        once: false,
        mirror: false
    });

    // Particles.js background for hero section
    if (document.getElementById('particles-js')) {
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 30, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#ffffff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.3, "random": true },
                "size": { "value": 5, "random": true },
                "move": {
                    "enable": true, "speed": 1, "direction": "top",
                    "random": true, "straight": false, "out_mode": "out"
                }
            },
            "interactivity": {
                "events": {
                    "onhover": { "enable": true, "mode": "bubble" },
                    "onclick": { "enable": true, "mode": "push" },
                    "resize": true
                },
                "modes": {
                    "bubble": {
                        "distance": 250, "size": 6,
                        "duration": 2, "opacity": 0.8, "speed": 3
                    },
                    "push": { "particles_nb": 4 }
                }
            },
            "retina_detect": true
        });
    }

    // Modal functionality for member bios
    const modal = document.getElementById('bioModal');
    const modalName = document.getElementById('modalName');
    const modalRole = document.getElementById('modalRole');
    const modalBio = document.getElementById('modalBio');
    const closeModal = document.getElementById('closeModal');
    const readMoreBtns = document.querySelectorAll('.read-more-btn');

    readMoreBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            modalName.textContent = btn.getAttribute('data-name');
            modalRole.textContent = btn.getAttribute('data-role');
            modalBio.textContent = btn.getAttribute('data-bio');
            modal.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        });
    });

    closeModal.addEventListener('click', function () {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    });

    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // Slide-up effect for .slide-up elements
    const slideElements = document.querySelectorAll('.slide-up');

    function checkSlide() {
        slideElements.forEach(element => {
            const slideInAt = (window.scrollY + window.innerHeight) - element.offsetHeight / 2;
            const elementBottom = element.offsetTop + element.offsetHeight;
            if (slideInAt > element.offsetTop && window.scrollY < elementBottom) {
                element.classList.add('visible');
            }
        });
    }

    window.addEventListener('scroll', checkSlide);
    checkSlide(); // On load

    // Hover color transition for member names
    const teamCards = document.querySelectorAll('.team-card');

    teamCards.forEach(card => {
        const nameElement = card.querySelector('.member-name');
        card.addEventListener('mouseenter', () => {
            nameElement.style.color = 'var(--accent-pink)';
        });
        card.addEventListener('mouseleave', () => {
            nameElement.style.color = 'var(--deep-blue)';
        });
    });
});

