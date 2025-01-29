// JAVASCRIPT KODAS DINAMIŠKAI GENERUOTI LENTELĘ SU DUOMENIMIS
document.addEventListener('DOMContentLoaded', function() {
    fetch('http://127.0.0.1:5000/api2/projektai')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('automobiliai-body');
            tbody.innerHTML = '';

            data.forEach(projektas => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${automobilis.id}</td>
                    <td>${automobilis.gamintojas}</td>
                    <td>${automobilis.modelis}</td>
                    <td>${automobilis.spalva}</td>
                    <td>${automobilis.salis}</td>
                    <td>${automobilis.kaina}</td>
                `;

                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

