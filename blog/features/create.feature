Feature: As create a post
	One user creates a new post and he looking for

	Scenario: I will create a post and view it
		Given I am at "http://127.0.0.1:8889/create/"
		Then I have title "My Test" and content "This is a little test"
		Then I put the data into the form and send form
		Then I am at "http://127.0.0.1:8889/posts/"