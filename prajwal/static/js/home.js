let welcome_page = document.querySelector('.welcome-page')
let panel_data_page = document.querySelector('.data-entry-page')

document.querySelector('.start-btn').addEventListener('click', () => {
    welcome_page.style.display = 'none'
    panel_data_page.style.display = 'block'
})