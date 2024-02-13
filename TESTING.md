# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- If you are copying/pasting your HTML code, use this link: https://validator.w3.org/#validate_by_input
- (*recommended*) If you are using the live deployed site pages, use this link: https://validator.w3.org/#validate_by_uri

It's recommended to validate the live pages (each of them) using the deployed URL.
This will give you a custom URL as well, which you can use on your testing documentation.
It makes it easier to return back to a page to validate it again in the future.
The URL will look something like this:

- https://validator.w3.org/nu/?doc=https%3A%2F%2FJamesH003.github.io%2Fflight_academy%2Findex.html

Sample HTML code validation documentation (tables are extremely helpful!):

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FJamesH003.github.io%2Fflight_academy%2Findex.html) | ![screenshot](documentation/html-validation-home.png) | Section lacks header h2-h6 warning |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FJamesH003.github.io%2Fflight_academy%2Fcontact.html) | ![screenshot](documentation/html-validation-contact.png) | obsolete iframe warnings |
| Quiz | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FJamesH003.github.io%2Fflight_academy%2Fquiz.html) | ![screenshot](documentation/html-validation-quiz.png) | Pass: No Errors |
| Add Blog | n/a | ![screenshot](documentation/html-validation-add-blog.png) | Duplicate IDs found, and fixed |
| Checkout | n/a | ![screenshot](documentation/html-validation-checkout.png) | Pass: No Errors |
| x | x | x | repeat for all remaining HTML files |

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**IMPORTANT**: Python/Jinja syntax in HTML

Python projects that use Jinja syntax, such as `{% for loops %}`, `{% url 'home' %}`, and `{{ variable|filter }}`
will not validate properly if you're copying/pasting into the HTML validator.

In order to properly validate these types of files, it's recommended to
[validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Unfortunately, pages that require a user to be logged-in and authenticated (CRUD functionality),
will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have
access to login to your pages.
In order to properly validate HTML pages with Jinja syntax for authenticated pages, follow these steps:

- Navigate to the deployed pages which require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- If you are copying/pasting your HTML code, use this link: https://jigsaw.w3.org/css-validator/#validate_by_input
- (*recommended*) If you are using the live deployed site, use this link: https://jigsaw.w3.org/css-validator/#validate_by_uri

It's recommended to validate the live site if you only have a single CSS file using the deployed URL.
This will give you a custom URL as well, which you can use on your testing documentation.
It makes it easier to return back to the page to validate it again in the future.
The URL will look something like this:

- https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2FJamesH003.github.io%2Fflight_academy

If you have multiple CSS files, then individual [validation by input](https://jigsaw.w3.org/css-validator/#validate_by_input)
is recommended for the additional CSS files.

**IMPORTANT**: Third-Party tools

If you're using extras like Bootstrap, Materialize, Font Awesome, then sometimes the validator
will attempt to also validate this code, even if it's not part of your own actual code.
You are not required to validate the external libraries or frameworks!

Sample CSS code validation documentation (tables are extremely helpful!):

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fflight-academy-e7e5adf022d9.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/testing/css-url-testing.png) | Pass: No Errors |
| payments.css | n/a | ![screenshot](documentation/testing/css-payments.png) | Pass: No Errors |
| user_profile.css | n/a | ![screenshot](documentation/testing/css-user-profile.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

If using modern JavaScript (ES6) methods, then make sure to include the following
line at the very top of every single JavaScript file (this should remain in your files for submission):

    /* jshint esversion: 11 */

If you are also including jQuery (`$`), then the updated format will be:

    /* jshint esversion: 11, jquery: true */

This allows the JShint validator to recognize modern ES6 methods, such as:
`let`, `const`, `template literals`, `arrow functions (=>)`, etc.

**IMPORTANT**: External resources

Sometimes we'll write JavaScript that imports variables from other files, such as an array of questions
from `questions.js`, which are used within the main `script.js` file elsewhere.
If that's the case, the JShint validation tool doesn't know how to recognize unused variables
that would normally be imported locally in your code.
These warnings are acceptable to showcase on your screenshots.

The same thing applies when using external libraries such as Stripe, Leaflet, Bootstrap, Materialize, etc..
To instantiate these components, we need to use their respective declarator.
Again, the JShint validation tool would flag these as undefined/unused variables.
These warnings are acceptable to showcase on your screenshots.

Sample JS code validation documentation (tables are extremely helpful!):

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

| File | Screenshot | Notes |
| --- | --- | --- |
| vouchers.html | ![screenshot](documentation/testing/js-vouchers.png) | Pass: No Errors |
| stripe_elements.js | ![screenshot](documentation/testing/js-stripe-elements.png) | Pass: No Errors |
| shopping_bag.html | ![screenshot](documentation/testing/js-shopping-bag.png) | Pass: No Errors |
| training.html | ![screenshot](documentation/testing/js-training.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| About urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/about/urls.py) | ![screenshot](documentation/testing/python-about-urls.png) | Pass: No Errors |
| About views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/about/views.py) | ![screenshot](documentation/testing/python-about-views.png) | Pass: No Errors |
| Contact admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/contact/admin.py) | ![screenshot](documentation/testing/python-contact-admin.png) | Pass: No Errors |
| Contact apps.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/contact/apps.py) | ![screenshot](documentation/testing/python-contact-apps.png) | Pass: No Errors |
| Contact forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/contact/forms.py) | ![screenshot](documentation/testing/python-contact-forms.png) | Pass: No Errors |
| Contact models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/contact/models.py) | ![screenshot](documentation/testing/python-contact-models.png) | Pass: No Errors |
| Contact urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/contact/urls.py) | ![screenshot](documentation/testing/python-contact-urls.png) | Pass: No Errors |
| Contact views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/contact/views.py) | ![screenshot](documentation/testing/python-contact-views.png) | Pass: No Errors |
| Flights admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/flights/admin.py) | ![screenshot](documentation/testing/python-flights-admin.png) | Pass: No Errors |
| Flights apps.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/flights/apps.py) | ![screenshot](documentation/testing/python-flights-apps.png) | Pass: No Errors |
| Flights forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/flights/forms.py) | ![screenshot](documentation/testing/python-flights-forms.png) | Pass: No Errors |
| Flights models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/flights/models.py) | ![screenshot](documentation/testing/python-flights-models.png) | Pass: No Errors |
| Flights urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/flights/urls.py) | ![screenshot](documentation/testing/python-flights-urls.png) | Pass: No Errors |
| Flights views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/flights/views.py) | ![screenshot](documentation/testing/python-flights-views.png) | Pass: No Errors |
| Home urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/home/urls.py) | ![screenshot](documentation/testing/python-home-urls.png) | Pass: No Errors |
| Home views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/home/views.py) | ![screenshot](documentation/testing/python-home-views.png) | Pass: No Errors |
| Newsletter admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/newsletter/admin.py) | ![screenshot](documentation/testing/python-newsletter-admin.png) | Pass: No Errors |
| Newsletter forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/newsletter/forms.py) | ![screenshot](documentation/testing/python-newsletter-forms.png) | Pass: No Errors |
| Newsletter models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/newsletter/models.py) | ![screenshot](documentation/testing/python-newsletter-models.png) | Pass: No Errors |
| Newsletter urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/newsletter/urls.py) | ![screenshot](documentation/testing/python-newsletter-urls.png) | Pass: No Errors |
| Payments admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/payments/admin.py) | ![screenshot](documentation/testing/python-payments-admin.png) | Pass: No Errors |
| Payments apps.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/payments/apps.py) | ![screenshot](documentation/testing/python-payments-apps.png) | Pass: No Errors |
| Payments forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/payments/forms.py) | ![screenshot](documentation/testing/python-payments-forms.png) | Pass: No Errors |
| Payments models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/payments/models.py) | ![screenshot](documentation/testing/python-payments-models.png) | Pass: No Errors |
| Payments signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/payments/signals.py) | ![screenshot](documentation/testing/python-payments-signals.png) | Pass: No Errors |
| Payments urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/payments/urls.py) | ![screenshot](documentation/testing/python-payments-urls.png) | Pass: No Errors |
| Payments views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/payments/views.py) | ![screenshot](documentation/testing/python-payments-views.png) | Pass: No Errors |
| Shopping_bag bag_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/shopping_bag/templatetags/bag_tools.py) | ![screenshot](documentation/testing/python-shopping-bagtools.png) | Pass: No Errors |
| Shopping_bag contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/shopping_bag/contexts.py) | ![screenshot](documentation/testing/python-shopping-contexts.png) | Pass: No Errors |
| Shopping_bag urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/shopping_bag/urls.py) | ![screenshot](documentation/testing/python-shopping-urls.png) | Pass: No Errors |
| Shopping_bag views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/shopping_bag/views.py) | ![screenshot](documentation/testing/python-shopping-views.png) | Pass: No Errors |
| Training admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/training/admin.py) | ![screenshot](documentation/testing/python-training-admin.png) | Pass: No Errors |
| Training forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/training/forms.py) | ![screenshot](documentation/testing/python-training-forms.png) | Pass: No Errors |
| Training models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/training/models.py) | ![screenshot](documentation/testing/python-training-models.png) | Pass: No Errors |
| Training urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/training/urls.py) | ![screenshot](documentation/testing/python-training-urls.png) | Pass: No Errors |
| Training views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/training/views.py) | ![screenshot](documentation/testing/python-training-views.png) | Pass: No Errors |
| User_profile models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/user_profile/models.py) | ![screenshot](documentation/testing/python-user_profile-models.png) | Pass: No Errors |
| User_profile urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/user_profile/urls.py) | ![screenshot](documentation/testing/python-user_profile-urls.png) | Pass: No Errors |
| User_profile views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/user_profile/views.py) | ![screenshot](documentation/testing/python-user_profile-views.png) | Pass: No Errors |
| flight_academy settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/flight_academy/settings.py) | ![screenshot](documentation/testing/python-flight-academy-settings.png) | Pass: No Errors |
| flight_academy urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/flight_academy/urls.py) | ![screenshot](documentation/testing/python-flight-academy-urls.png) | Pass: No Errors |
| flight_academy urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/flight_academy/main/flight_academy/views.py) | ![screenshot](documentation/testing/python-flight-academy-views.png) | Pass: No Errors |

## Browser Compatibility

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to discuss testing the live/deployed site on various browsers.

Consider testing at least 3 different browsers, if available on your system.

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the tested browsers, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time.
Some of these are paid services, but some are free.
If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

Sample browser testing documentation:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Training | Vouchers | About | Contact Us | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome-home-desktop.png) | ![screenshot](documentation/chrome-training-desktop.png) | ![screenshot](documentation/chrome-vouchers-desktop.png) | ![screenshot](documentation/chrome-about-desktop.png) | ![screenshot](documentation/chrome-contact-desktop.png) | Works as expected |
| Firefox | ![screenshot](documentation/firefox-home-desktop.png) | ![screenshot](documentation/firefox-training-desktop.png) | ![screenshot](documentation/firefox-vouchers-desktop.png) | ![screenshot](documentation/firefox-about-desktop.png) | ![screenshot](documentation/firefox-contact-desktop.png) | Works as expected |
| Edge | ![screenshot](documentation/edge-home-desktop.png) | ![screenshot](documentation/edge-training-desktop.png) | ![screenshot](documentation/edge-vouchers-desktop.png) | ![screenshot](documentation/edge-about-desktop.png) | ![screenshot](documentation/edge-contact-desktop.png) | Works as expected |
| Safari | ![screenshot](documentation/safari-home-desktop.png) | ![screenshot](documentation/safari-training-desktop.png) | ![screenshot](documentation/safari-vouchers.desktop.png) | ![screenshot](documentation/safari-about-desktop.png) | ![screenshot](documentation/safari-contact-desktop.png) | Works as expected |
| Brave | ![screenshot](documentation/brave-home-desktop.png) | ![screenshot](documentation/brave-training-desktop.png) | ![screenshot](documentation/brave-vouchers-desktop.png) | ![screenshot](documentation/brave-about-desktop.png) | ![screenshot](documentation/brave-contact-desktop.png) | Works as expected |
| Opera | ![screenshot](documentation/opera-home-desktop.png) | ![screenshot](documentation/opera-training-desktop.png) | ![screenshot](documentation/opera-voucher-desktop.png) | ![screenshot](documentation/opera-about-desktop.png) | ![screenshot](documentation/opera-contact-desktop.png) | Works as expected |

## Responsiveness

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is for the following 3 tests:
- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of the tested responsiveness, to "prove" that you've actually tested them.

Using the "amiresponsive" mockup image (or similar) does not suffice the requirements.
Consider using some of the built-in device sizes in the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well.
It showcases a higher level of manual tests, and can be seen as a positive inclusion!

Sample responsiveness testing documentation:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Training | Vouchers | About | Contact | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/mobile-devtools-home.png) | ![screenshot](documentation/mobile-devtools-training.png) | ![screenshot](documentation/mobile-devtools-vouchers.png) | ![screenshot](documentation/mobile-devtools-about.png) | ![screenshot](documentation/mobile-devtools-contact.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/tablet-devtools-home.png) | ![screenshot](documentation/tablet-devtools-training.png) | ![screenshot](documentation/tablet-devtools-vouchers.png) | ![screenshot](documentation/tablet-devtools-about.png) | ![screenshot](documentation/tablet-devtools-contact.png) | Works as expected |
| Desktop | ![screenshot](documentation/chrome-home-desktop.png) | ![screenshot](documentation/chrome-training-desktop.png) | ![screenshot](documentation/chrome-vouchers-desktop.png) | ![screenshot](documentation/chrome-about-desktop.png) | ![screenshot](documentation/chrome-contact-desktop.png) | Works as expected |
| iPhone 11 | ![screenshot](documentation/home-iphone11.PNG) | ![screenshot](documentation/training-iphone11.PNG) | ![screenshot](documentation/vouchers-iphone11.PNG) | ![screenshot](documentation/about-iphone11.PNG) | ![screenshot](documentation/contact-iphone11.PNG) | Works as expected |
| iPad | ![screenshot](documentation/home-ipad.PNG) | ![screenshot](documentation/training-ipad.PNG) | ![screenshot](documentation/voucher-ipad.PNG) | ![screenshot](documentation/about-ipad.PNG) | ![screenshot](documentation/ipad-contact.png) | Last letter in training and vouchers cards wraps to next line |


## Lighthouse Audit

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

If you don't have Lighthouse in your Developer Tools,
it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Don't just test the home page (unless it's a single-page application).
Make sure to test the Lighthouse Audit results for all of your pages.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

Sample Lighthouse testing documentation:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-mobile-home.png) | ![screenshot](documentation/lighthouse-desktop-home.png) | Some minor warnings |
| Training | ![screenshot](documentation/lighthouse-mobile-training.png) | ![screenshot](documentation/lighthouse-desktop-training.png) | Slow response time due to large images |
| Vouchers | ![screenshot](documentation/lighthouse-mobile-vouchers.png) | ![screenshot](documentation/lighthouse-desktop-vouchers.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse-mobile-about.png) | ![screenshot](documentation/lighthouse-desktop-about.png) | Some minor warnings |
| Contact | ![screenshot](documentation/lighthouse-mobile-contact.png) | ![screenshot](documentation/lighthouse-desktop-contact.png) | Some minor warnings |
| Voucher Details | ![screenshot](documentation/lighthouse-mobile-voucher-details.png) | ![screenshot](documentation/lighthouse-desktop-voucher-details.png) | Some minor warnings |
| Training Details | ![screenshot](documentation/lighthouse-mobile-training-details.png) | ![screenshot](documentation/lighthouse-desktop-training-details.png) | Some minor warnings |
| Shopping Bag | ![screenshot](documentation/lighthouse-mobile-shopping-bag.png) | ![screenshot](documentation/lighthouse-desktop-shopping-bag.png) | Some minor warnings |
| Payments Success | ![screenshot](documentation/lighthouse-mobile-payments-success.png) | ![screenshot](documentation/lighthouse-desktop-payments-success.png) | Some minor warnings |
| Register | ![screenshot](documentation/lighthouse-mobile-register.png) | ![screenshot](documentation/lighthouse-desktop-register.png) | Some minor warnings |
| User Profile | ![screenshot](documentation/lighthouse-mobile-user-profile.png) | ![screenshot](documentation/lighthouse-desktop-user-profile.png) | Some minor warnings |

## Defensive Programming

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Training | | | | | |
| | From the training page a user should be able to view the training courses, but not add new ones, unless the user is a superuser | Tested the feature by logging in as a non-superuser | The feature behaved as expected, and the Add Training Course button was not displayed | Test concluded and passed | ![screenshot](documentation/defprog-training-add-training.png) |
| | From the training page a user should be able to view the training courses, but not add new ones, unless the user is a superuser | Tested the feature by logging in as a non-superuser and trying to access the page through the add_training url directly | The feature behaved as expected, and a 500 error page was displayed with a warning toast | Test concluded and passed | ![screenshot](documentation/deefprog-training-add-url.png) |
| | From the training page a user should be able to view the training courses, but not add new ones, unless the user is a superuser | Tested the feature by not logging in at all and trying to access the page through the add_training url directly | The feature behaved as expected, and displayed the Signin page | Test concluded and passed | ![screenshot](documentation/defprog-training-add-not-logged-in.png) |
| | From the training page a user should be able to view the training courses, but not edit or delete, unless the user is a superuser | Tested the feature by not logging in at all and trying to access the page through the edit url directly | The feature behaved as expected, and displayed the Signin page | Test concluded and passed | ![screenshot](documentation/defprog-training-edit-not-logged-in.png) |
| | From the training details page a user should be able to view the training courses, but not edit or delete, unless the user is a superuser | Tested the feature by logging in as a non-superuser | The feature behaved as expected, and the Edit and Delete buttons were not displayed | Test concluded and passed | ![screenshot](documentation/defprog-training-edit.png) |
| | From the training details page a superuser should not be able to delete a training courses without a warning modal to confirm their decision. | Tested the feature by logging in as a superuser and clicking delete | The feature behaved as expected, and the Delete modal was displayed | Test concluded and passed | ![screenshot](documentation/defprog-training-delete-modal.png) |
| | From the training details page a user should be able to view the training courses, but not edit or delete, unless the user is a superuser | Tested the feature by logging in as a non-superuser and trying to access the page through the edit url directly | The feature behaved as expected, and the edit page was not accessed and a warning toast was displayed | Test concluded and passed | ![screenshot](documentation/defprog-training-edit-url.png) |
| Vouchers | | | | | |
| | From the vouchers page a user should be able to view the vouchers, but not add new ones, unless the user is a superuser | Tested the feature by logging in as a non-superuser | The feature behaved as expected, and the Add Voucher button was not displayed | Test concluded and passed | ![screenshot](documentation/defprog-vouchers-add.png) |
| | From the vouchers page a user should be able to view the vouchers, but not add new ones, unless the user is a superuser | Tested the feature by logging in as a non-superuser and trying to access the page through the add_voucher url directly | The feature behaved as expected, and a 500 error page was displayed with a warning toast | Test concluded and passed | ![screenshot](documentation/defprog-vouchers-add-url.png) |
| | From the vouchers page a user should be able to view the vouchers, but not add new ones, unless the user is a superuser | Tested the feature by not logging in at all and trying to access the page through the add_voucher url directly | The feature behaved as expected, and displayed the Signin page | Test concluded and passed | ![screenshot](documentation/defprog-vouchers-add-not-logged-in.png) |
| | From the vouchers page a user should be able to view the vouchers, but not Edit or Delete, unless the user is a superuser | Tested the feature by not logging in at all and trying to access the page through the edit url directly | The feature behaved as expected, and displayed the Signin page | Test concluded and passed | ![screenshot](documentation/defprog-vouchers-edit-not-logged-in.png) |
| | From the voucher details page a user should be able to view the voucher details, but not edit or delete, unless the user is a superuser | Tested the feature by logging in as a non-superuser | The feature behaved as expected, and the Edit and Delete buttons were not displayed | Test concluded and passed | ![screenshot](documentation/defprog-vouchers-edit.png) |
| | From the voucher details page a superuser should not be able to delete a voucher without a warning modal to confirm their decision. | Tested the feature by logging in as a superuser and clicking delete | The feature behaved as expected, and the Delete modal was displayed | Test concluded and passed | ![screenshot](documentation/defprog-vouchers-delete.png) |
| | From the voucher details page a user should be able to view the vouchers, but not edit or delete, unless the user is a superuser | Tested the feature by logging in as a non-superuser and trying to access the page through the edit url directly | The feature behaved as expected, and the edit page was not accessed and a warning toast was displayed | Test concluded and passed | ![screenshot](documentation/defprog-vouchers-edit-url.png) |
| User Profile | | | | | |
| | A user should only be able to view their user profile and order history when they're logged in. | Tested the feature by not logging in and trying to access the page using the user_profile url | The feature behaved as expected, and the Signin page was displayed | Test concluded and passed | ![screenshot](documentation/defprog-user-profile-url.png) |
| | A user should only be able to view their user profile and order history when they're logged in. | Tested the feature by not logging in and trying to access the page using account dropdown menu in the navbar. | The feature behaved as expected, and the Profile link was not displayed | Test concluded and passed | ![screenshot](documentation/defprog-user-profile-profile.png) |
| Newsletter | | | | | |
| | To sign up for the newsletter, a user should not be able to submit a blank form | Tested the feature by leaving the email input field black and clicking submit | The feature behaved as expected and an error message appeared requesting the user fill in the field. | Test concluded and passed | ![screenshot](documentation/defprog-newsletter-blank-form.png) |
| Payments | | | | | |
| | To complete the payment flow users shouldn't be able to leave input fields blank | Tested the feature by leaving the input fields blank and clicking Complete Order | The feature behaved as expected and an error message appeared requesting the user fill in the fields. | Test concluded and passed | ![screenshot](documentation/defprog-payments-blank-form.png) |
| | To complete the payment flow users shouldn't be able to leave card input blank | Tested the feature by leaving the input field blank and clicking Complete Order | The feature behaved as expected and an error message appeared stating that the card number is incomplete. | Test concluded and passed | ![screenshot](documentation/defprog-payments-stripe.png) |


## User Story Testing

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to view a list of products, so that I can decide which one to purchese. | ![screenshot](documentation/features/features-vouchers.png) |
| As a new site user, I would like to view individual product details, so that I can decide which one I want to purchase. | ![screenshot](documentation/features/features-voucher-details.png) |
| As a new site user, I would like to clearly see the types of products available, so that I can select the appropriate one. | ![screenshot](documentation/features/features-vouchers.png) |
| As a new site user, I would like to easily add a product to my shopping bag, so that I can purchase the product. | ![screenshot](documentation/features/features-voucher-details.png) |
| As a new site user, I would like to view the items in my bag to be purchased, so that I can know which products I have selected. | ![screenshot](documentation/features/features-shopping-bag.png) |
| As a new site user, I would like to adjust the quantity of products in my bag, so that I can increase or decrease the number of products I want to purchase. | ![screenshot](documentation/features/features-shopping-bag.png) |
| As a new site user, I would like to easily view the total price of my purchases, so that I can stay aware of my spending. | ![screenshot](documentation/user-stories-view-cost.png) |
| As a new site user, I would like to easily enter my payment information, so that I can pay for my chosen products with great ease. | ![screenshot](documentation/features/features-checkout-page.png) |
| As a new site user, I would like to view an order confirmation after checkout, so that I can have a record of what I have ordered. | ![screenshot](documentation/features/features-order-confirmation.png) |
| As a new site user, I would like to receive an email confirmation, so that I can have proof of purchase. | ![screenshot](documentation/features/features-order-confirmation.png) |
| As a new site user, I would like to subscribe to a newsletter, so that I can get more information. | ![screenshot](documentation/features/features-newsletter.png) |
| As a new site user, I would like to view different training courses, so that I can assess my options. | ![screenshot](documentation/features/features-training-page.png) |
| As a returning site user, I would like to register an account, so that I can have a personal account. | ![screenshot](documentation/features/features-register.png) |
| As a returning site user, I would like to login to my account, so that I can access my personal account. | ![screenshot](documentation/features/features-signin.png) |
| As a returning site user, I would like to logout of my account, so that I can logout of my personal account. | ![screenshot](documentation/user-story-signout.png) |
| As a returning site user, I would like to recover my password, so that I can regain access to my account. | ![screenshot](documentation/user-story-forgot-password.png) |
| As a returning site user, I would like to know my information is secure, so that I can be confident in entering my payment information. | ![screenshot](documentation/features/features-checkout-page.png) |
| As a returning site user, I would like to access links to social media pages, so that I can view their social media content. | ![screenshot](documentation/features/features-footer.png) |
| As a site administrator, I should be able to add new products to the store, so that I can increase the amount of products on offer. | ![screenshot](documentation/features/features-add-training.png) |
| As a site administrator, I should be able to edit or update products, so that I can keep the product information up to date. | ![screenshot](documentation/features/features-edit-delete.png) |
| As a site administrator, I should be able to delete products from the store, so that I can remove products that are no longer for sale. | ![screenshot](documentation/features/features-edit-delete.png) |
| As a site administrator, I should be able to add new training course options, so that I can improve what the site has to offer. | ![screenshot](documentation/features/features-add-training.png) |
| As a site administrator, I should be able to edit training courses, so that I can change certain aspects as needs be. | ![screenshot](documentation/features/features-edit-delete.png) |
| As a site administrator, I should be able to delete training courses, so that I can remove courses that are no longer available. | ![screenshot](documentation/features/features-edit-delete.png) |

## Bugs

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/JamesH003/flight_academy/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/JamesH003/flight_academy/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/JamesH003/flight_academy/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/JamesH003/flight_academy/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/JamesH003/flight_academy/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/JamesH003/flight_academy/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/JamesH003/flight_academy/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/JamesH003/flight_academy/issues/5) | Open |

## Unfixed Bugs

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

<!-- 🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑 -->

There are no remaining bugs that I am aware of.
