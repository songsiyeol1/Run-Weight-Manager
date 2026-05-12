const dates = JSON.parse(
    document.getElementById('dates-data').textContent
);

const weights = JSON.parse(
    document.getElementById('weights-data').textContent
);

const runkms = JSON.parse(
    document.getElementById('runkms-data').textContent
);

const ctx = document.getElementById('weightChart');

new Chart(ctx, {

    data: {

        labels: dates,

        datasets: [

            {
                type: 'bar',

                label: '달리기 거리 (km)',

                data: runkms,

                borderRadius: 10
            },

            {
                type: 'line',

                label: '몸무게 (kg)',

                data: weights,

                borderWidth: 3,

                tension: 0.3
            }
        ]
    }
});