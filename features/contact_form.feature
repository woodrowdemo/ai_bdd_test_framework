Feature: Contact Us form functionality

    Scenario: Valid form submission
        Given I am on the Contact Us form
        When I fill in the 'First Name' field with "John"
        And I fill in the 'Last Name' field with "Doe"
        And I fill in the 'Email Address' field with "johndoe@example.com"
        And I fill in the 'Comments' field with "This is a test message"
        And I click on the 'SUBMIT' button
        Then I should see the success message: "Thank You for your Message"

    Scenario: Missing fields
        Given I am on the Contact Us form
        When I click on the 'SUBMIT' button
        Then I should see the error message: "Error: All fields are required"

    Scenario: Invalid email address
        Given I am on the Contact Us form
        When I fill in the 'First Name' field with "Jane"
        And I fill in the 'Last Name' field with "Smith"
        And I fill in the 'Email Address' field with "invalidemail.com"
        And I fill in the 'Comments' field with "This is another test message"
        And I click on the 'SUBMIT' button
        Then I should see the error message: "Error: Invalid email address"

    Scenario: Using the 'RESET' button
        Given I am on the Contact Us form
        When I fill in all fields
        And I click on the 'RESET' button
        Then all fields should be cleared