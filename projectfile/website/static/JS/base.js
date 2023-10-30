const icons = document.querySelectorAll('.icon');

  icons.forEach((icon) => {
    icon.addEventListener('mouseover', () => {
      icon.classList.add('fa-regular');
      icon.classList.remove('fa-solid');
    });

    icon.addEventListener('mouseout', () => {
      icon.classList.add('fa-solid');
      icon.classList.remove('fa-regular');
    });
  });