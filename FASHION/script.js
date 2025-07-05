document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".slider");
    const slides = document.querySelectorAll(".slide");
    const slideWidth = slides[0].clientWidth;
    let index = 0;
    VanillaTilt.init(document.querySelectorAll(".upload-box"), {
        max: 15,
        speed: 400,
        glare: true,
        "max-glare": 0.3,
    });
    

    // Clone slides for infinite effect
    slides.forEach(slide => {
        const clone = slide.cloneNode(true);
        slider.appendChild(clone);
    });

    function slideImages() {
        index++;
        slider.style.transition = "transform 0.5s ease-in-out";
        slider.style.transform = `translateX(-${index * slideWidth}px)`;

        // Reset when it reaches the last cloned slide
        setTimeout(() => {
            if (index >= slides.length) {
                index = 0;
                slider.style.transition = "none"; // Remove transition for instant reset
                slider.style.transform = `translateX(0)`;
            }
        }, 500);
    }

    setInterval(slideImages, 3000); // Slide every 3 seconds
});

function previewImage(event, previewId) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.getElementById(previewId);
            preview.src = e.target.result;
            preview.style.display = "block";
        }
        reader.readAsDataURL(file);
    }
}