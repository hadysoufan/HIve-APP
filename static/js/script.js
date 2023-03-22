'use strict';

///////////////////////////////////////////////////////////
// Loader
window.addEventListener('load', function () {
  document.querySelector('main').style.display = 'none';
  document.querySelector('footer').style.display = 'none';
  document.querySelector('.honeycomb').style.display = 'block';
  setTimeout(function () {
    document.querySelector('.honeycomb').style.display = 'none';
    document.querySelector('main').style.display = 'block';
    document.querySelector('footer').style.display = 'block';
  }, 500);
});

////////////////////////
// reveal elements on scroll
const allSections = document.querySelectorAll('.section');

const revealSection = function (entries, observer) {
  const [entry] = entries;

  if (!entry.isIntersecting) {
    return;
  }

  entry.target.classList.remove('section--hidden');

  observer.unobserve(entry.target);
};

const sectionObserver = new IntersectionObserver(revealSection, {
  root: null,
  threshold: 0.15,
});

allSections.forEach(function (section) {
  sectionObserver.observe(section);
  section.classList.add('section--hidden');
});

///////////////////////////////////////////////////////////
// Scroll up
const scrollBtn = document.querySelector('.scroll-up-btn');
scrollBtn.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  });
});

///////////////////////////////////////////////////////////
// Sticky navigation

const sectionHeroEl = document.querySelector('.section-hero');

const obs = new IntersectionObserver(
  function (entries) {
    const ent = entries[0];
    console.log(ent);

    if (ent.isIntersecting === false) {
      document.body.classList.add('sticky');
    }

    if (ent.isIntersecting === true) {
      document.body.classList.remove('sticky');
    }
  },
  {
    // In the viewport
    root: null,
    threshold: 0,
    rootMargin: '-80px',
  }
);
obs.observe(sectionHeroEl);

///////////////////////////////////////////////////////////
// Testimonials section

const testimonialsContainer = document.querySelector('.testimonials-container');
const testimonial = document.querySelector('.testimonial');
const userImage = document.querySelector('.user-image');
const username = document.querySelector('.username');
const role = document.querySelector('.role');

const testimonials = [
  {
    name: 'Jonathan Walters',
    position: 'Verified User',
    photo:
      'https://raw.githubusercontent.com/RahulSahOfficial/testimonials_grid_section/5532c958b7d3c9b910a216b198fdd21c73112d84/images/image-kira.jpg',
    text: 'The video chat quality is fantastic and the ability to shop and share stories with my friends has made it my go-to social media.',
  },
  {
    name: 'Kira Whittle',
    position: 'Verified User',
    photo:
      'https://raw.githubusercontent.com/RahulSahOfficial/testimonials_grid_section/5532c958b7d3c9b910a216b198fdd21c73112d84/images/image-kira.jpg',
    text: "I've been searching for a social media platform that puts privacy first, and Hive does just that.The security features give me peace of mind and the option to connect with friends and family fromall over the world is just icing on the cake.",
  },
  {
    name: 'Jeanette Harmon',
    position: 'Verified User',
    photo:
      'https://raw.githubusercontent.com/RahulSahOfficial/testimonials_grid_section/5532c958b7d3c9b910a216b198fdd21c73112d84/images/image-jeanette.jpg',
    text: "The ability to connect with friends and family in real-time through video chats and the option to shop and share stories make it a must-have app. I've never seen a social media platform thatcombines so many great features into one app. I highly recommend giving Hive a try.",
  },
  {
    name: 'Patrick Abrams',
    position: 'Verified User',
    photo:
      'https://raw.githubusercontent.com/RahulSahOfficial/testimonials_grid_section/5532c958b7d3c9b910a216b198fdd21c73112d84/images/image-patrick.jpg',
    text: "I've been using Hive for a few months now and I am thoroughly impressed. The video chat featureis seamless, and the option to shop and post stories has made it a staple in my daily routine. Ilove the customization options for my profile page, it makes my social media experience trulyunique. I highly recommend giving Hive a try, you won't be disappointed!",
  },
  {
    name: 'Jonathan Nunfiez',
    position: 'Graphic Designer',
    photo: 'https://randomuser.me/api/portraits/men/43.jpg',
    text: "I had my concerns that due to a tight deadline this project can't be done. But this guy proved me wrong not only he delivered an outstanding work but he managed to deliver 1 day prior to the deadline. And when I asked for some revisions he made them in MINUTES. I'm looking forward to work with him again and I totally recommend him. Thanks again!",
  },
];

let idx = 1;

function updateTestimonial() {
  const { name, position, photo, text } = testimonials[idx];

  testimonial.innerHTML = text;
  userImage.src = photo;
  username.innerHTML = name;
  role.innerHTML = position;

  idx++;

  if (idx > testimonials.length - 1) {
    idx = 0;
  }
}

setInterval(updateTestimonial, 10000);
