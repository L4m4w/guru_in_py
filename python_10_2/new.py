from selene import browser, be, have

browser.config.window_width = 720
browser.config.window_height = 480

browser.open('https://demoqa.com/text-box')
browser.element('[id="userName"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="submit"]').click()
browser.element('[id="output"]').should(have.text('yashaka/selene'))