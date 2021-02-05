document.querySelector('#load-image').addEventListener('input',loadImage)

function loadImage(e){
    const ctx = document.querySelector('#canvas').getContext('2d')
    let url = URL.createObjectURL(e.target.files[0])
    let image = new Image()
    image.src = url
    image.onload = () => {
        ctx.drawImage(image,0,0)
    }
    let data = ctx.getImageData(0,0,200,200).data
    inputRadiation(getRadiation(getBrightness(data)))
}

function getBrightness(data){
    let r,g,b,avg
    let count = 0
    let totalAvg = 0
    for(let i=0;i<data.length;i+=4){
        r = data[i]
        g = data[i+1]
        b = data[i+2]
        avg = Math.floor((r+g+b)/3)
        count += 1
        totalAvg += avg
    }
    return Math.floor(totalAvg/count)
}

function getRadiation(brightness){
    return (200/51)*brightness
}

function inputRadiation(radiation){
    document.querySelector('#radiation').textContent = radiation
    fetchRadiation(radiation)
}

document.querySelector('#find-me').addEventListener('click', geoFindMe)

function geoFindMe() {
    const status = document.querySelector('#status');
    const location = document.querySelector('#location')

    location.textContent = ''

    function success(position) {
        const latitude  = position.coords.latitude
        const longitude = position.coords.longitude
        status.textContent = ''
        document.querySelector('#find-me').style.display = 'none'
        let loc = `${latitude},${longitude}`
        location.textContent = loc
        fetchLocation(loc)
    }

    function error() {
        status.textContent = 'Unable to retrieve your location'
        alert('we are currently unable to recive your location, so your request goes with default lacation')
        loc = '21.8,80.9'
        location.textContent = loc
        fetchLocation(loc)
    }

    if(!navigator.geolocation) {
        status.textContent = 'Geolocation is not supported by your browser'
    } else {
        status.textContent = 'Locating…'
        navigator.geolocation.getCurrentPosition(success, error)
    }
}

function fetchLocation(location){
    fetch('/location',{
        method:'POST',
        headers:{
            'content-type':'application/json'
        },
        body:JSON.stringify({
            location:location
        })
    }).then((res)=>{
        return res.json()
    }).then((msg)=>{
        console.log(msg.message)
    })
    .catch((err)=>console.log(err))
}

function fetchRadiation(radiation){
    fetch('/radiation',{
        method:'POST',
        headers:{
            'content-type':'application/json'
        },
        body:JSON.stringify({
            radiation:radiation
        })
    }).then((res)=>{
        return res.json()
    }).then((msg)=>{
        console.log('done')
    })
    .catch((err)=>console.log(err))
}