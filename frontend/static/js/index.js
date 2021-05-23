async function callClick() {
    let response = await fetch('/click/', {
        method: 'GET'
    });
    let answer = await response.json();
    document.getElementById("data").innerHTML = answer.coinsCount;
    if (answer.boosts)
        renderAllBoosts(answer.boosts);
}

async function getUser(id){
    let response = await fetch('/users/' + id, {
        method: 'GET'
    });
    let answer = await response.json();
    document.getElementById("user").innerHTML = answer['username'];
    let getCycle = await fetch('/cycles/' + answer['cycle'],{
        method: 'GET'
    });
    let cycle = await getCycle.json();
    document.getElementById("data").innerHTML = cycle['coinsCount'];
    document.getElementById("clickPower").innerHTML = cycle['clickPower'];
    let boostRequest = await fetch('/boosts/' + answer['cycle'], {
        method: 'GET'
    });
    let boosts = await boostRequest.json();
    renderAllBoosts(boosts);
}

function buyBoost(boost_level){
    const csrftoken = getCookie('csrftoken')
    fetch('/buyBoost/', {
        method: 'POST',
        headers: {
            "X-CSRFToken": csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            boost_level: boost_level
        })
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return Promise.reject(response);
        }
    }).then(data => {
        document.getElementById("data").innerHTML = data['coinsCount'];
        document.getElementById(`clickPower_${boost.level}`).innerHTML = data['clickPower'];
        document.getElementById(`boostLevel_${boost.level}`).innerHTML = data['level'];
        document.getElementById(`boostPrice_${boost.level}`).innerHTML = data['price'];
        document.getElementById(`boostPower_${boost.level}`).innerHTML = data['power'];
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring((name.length + 1)));
                break;
            }
        }
    }
    return cookieValue;
}

function renderAllBoosts(boosts) {
    let parent = document.getElementById('boost-wrapper');
    parent.innerHTML = '';
    boosts.forEach(boost => {
        renderBoost(parent, boost);
    })
}

function renderBoost(parent, boost) {
    const div = document.createElement('div');
    div.setAttribute('class', 'boost-holder');
    div.setAttribute('id', `boost-holder-${boost.level}`);
    div.innerHTML = `
    <div class="boost-holder" id ="boost-holder">
      <input type="image" class="money boost" onclick="buyBoost(${boost.level})">
      <p> Level: <div id="boostLevel_${boost.level}">  ${boost.level} </div></p>
      <p> Power: <div id="boostPower_${boost.level}">  ${boost.power} </div></p>
      <p> Price: <div id="boostPrice_${boost.level}">  ${boost.price} </div></p>
    </div>`;
    parent.appendChild(div);
}