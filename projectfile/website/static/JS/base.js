
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

  $(document).ready(function() {
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 2000);
  });       
  

  function submitdietForm() {
    document.getElementById("filterdietForm").submit();
}

function submitthemeForm() {
  document.getElementById("filterthemeForm").submit();
}

function submitSLForm() {
  document.getElementById("filterSLForm").submit();
}
  