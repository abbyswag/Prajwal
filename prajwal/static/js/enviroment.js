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
    // console.log(totalAvg)
    return Math.floor(totalAvg/count)
}

function getRadiation(brightness){
    // console.log(brightness)
    return (200/51)*brightness
}

function inputRadiation(radiation){
    // console.log(radiation)
    document.querySelector('#radiation').value = radiation
}