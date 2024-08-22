
        function showSidebar(){
            const sidebar = document.querySelector(".sidebar");
            sidebar.style.display = "flex";
        }

        function closeSidebar(){
            const sidebar = document.querySelector(".sidebar");
            sidebar.style.display = "none";
        }


    document.querySelector('.arrow-down').addEventListener('click', function() {
        document.getElementById('about').scrollIntoView({ behavior: 'smooth' });
    });

