fetch('/data/output',{
    headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
})
.then((res) => {
    return res.json()
})
.then((data) => {
    document.getElementById('electricPower').textContent = data.electricPower
    document.getElementById('efficiency').textContent = data.efficiency
    document.getElementById('temprature').textContent = data.temprature
    document.getElementById('inclination').textContent = data.inclination
    document.getElementById('orientation').textContent = data.orientation
})
.catch(err => console.error(err))