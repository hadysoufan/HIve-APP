// side bar

let menuItems = document.querySelectorAll('.menu-item');

const changeActiveItem = () => {
  menuItems.forEach((item) => {
    item.classList.remove('active');
  });
};

menuItems.forEach((item) => {
  item.addEventListener('click', () => {
    changeActiveItem();
    item.classList.add('active');
    if (item.id != 'notifications') {
      document.querySelector('.notification-popup').style.display = 'none';
    } else {
      document.querySelector('.notification-popup').style.display = 'block';
      document.querySelector(
        '#notifications .notification-count'
      ).style.display = 'none';
    }
  });
});

// messages

const messagesNotifactions = document.querySelector('#messages-notifications');
const messages = document.querySelector('.messages');
const message = messages.querySelectorAll('.message');
const messageSearch = document.querySelector('#message-search');

messagesNotifactions.addEventListener('click', () => {
  messages.style.boxShadow = '0 0 1rem var(--color-primary)';
  messagesNotifactions.querySelector('.notification-count').style.display =
    'none';
  setTimeout(() => {
    messages.style.boxShadow = 'none';
  }, 2000);
});

const searchMessage = () => {
  const val = messageSearch.value.toLowerCase();
  message.forEach((user) => {
    let name = user.querySelector('h5').textContent.toLowerCase();
    if (name.indexOf(val) != -1) {
      user.style.display = 'flex';
    } else {
      user.style.display = 'none';
    }
  });
};

messageSearch.addEventListener('keyup', searchMessage);


const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnsOpenModal = document.querySelectorAll('.show-modal');

const openModal = function () {
  console.log('Buttom Clicked');
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};

const closeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

for (let i = 0; i < btnsOpenModal.length; i++) {
  btnsOpenModal[i].addEventListener('click', openModal);
}

btnCloseModal.addEventListener('click', closeModal);

overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
    closeModal();
  }
});