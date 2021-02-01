let welcome_page = document.querySelector('.welcome-page')
let user_page = document.querySelector('#user-page')
let panel_page = document.querySelector('#panel-page')
let enviroment_page = document.querySelector('#enviroment-page')

document.querySelector('.get-user-page').addEventListener('click',() => {
    user_page.style.display = 'block'
    welcome_page.style.display = 'none'
})
document.querySelector('.get-panel-page').addEventListener('click',() => {
    panel_page.style.display = 'block'
    user_page.style.display = 'none'
})
document.querySelector('.get-enviroment-page').addEventListener('click',() => {
    enviroment_page.style.display = 'block'
    panel_page.style.display = 'none'
})