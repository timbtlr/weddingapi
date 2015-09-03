# Wedding Site
## Pages
* Home
* About Us
* About the Wedding
* RSVP
    * RSVP objects
        * GET (super/admin users)
        * POST (standard users)
* Pictures
    * Image ojects
        * GET (anonymous)
        * POST (super/admin users)
* Registry
    * Registry link objects
        * GET (anonymous)
        * PUT (standard users)
        * POST (super/admin)

## Authentication
Authentication is handled by Json Web Tokens (JWTs).  Each action HTTP request ensures that the user is authorized before sending a response.

## Users
Anonymous users will not be able to setup new accounts.  Instead, users of the site are provided a username/password combination.

### Standard Users
Standard users are to be used by guests.  Standard users are allowed the following privledges:
- View photos
- Add an RSVP
- View registry items
- Edit the status of existing registry items

Standard users do not have to input a username.  Instead, they are prompted for a code (setup as a standard user account password) when editing registry or RSVP resources.

### Admin / Super Users
Admin users must login to the site to access additional website options.  Admin users have all of the same privledges of a standard user along with the following benefits:
- Edit existing photos
- Add photos
- Edit existing registry items
- Add registry items
- View RSVPs
- Edit existing RSVPs

## Object Definitions
### RSVP
```
{
   "id": "1",
   "name": "John Doe",
   "attending": "true",
   "plus_one": "true", //optional
   "food_choice": "buffet",
   "drink_choice": "IPA"
}
```
### Pictures
```
{
   "id": "1",
   "full_url": "www.someplace.com/picture.jpg",
   "caption": "This is a picture of stuff",
}
```
### Registry Items
```
{
   "id": "1",
   "name": "Teapot",
   "full_url": "www.target.com/teapot",
   "description": "Steel teapot with handle",
   "price": "100.00",
   "store": "Target",
   "bought": "false"
}
```
