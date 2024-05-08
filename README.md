# building steps

view user profile
edit user profile


create Hoot
    the model
    url pathing with userID/postID
    likers
view a Hoot




since replies are tied to Originals, see if you can have a module within a module
create a reply
    includes author (foreign key)
    post date (since there's no edit)
    likers? (do we store liked messages inside a user, or store users inside the message, or do we store likers inside the original message thread?)

view a reply

attach a reply (foreign key) to a post






# Tweeter (Twitter clone)
A live demo will be hosted on Heroku

## Author's context:
Last week, I published my first homegrown CRUD: [Yindeed](https://github.com/martn2023/yindeed1/blob/master/README.md). The learnings and feedback from mentors has driven the following goals for this project:

## What I built:
>**Overview:**<br>
Hootter is like a Twitter, but for a wiser crowd to share wisdom.

>* user A can create an "Original Post":
>  * users A or B can "Reply" to Original Post, but not to a Reply
>  * replies from B show up in A's "Feed"
>* user A can subscribe to user B:
>  * in A's Feed, B's Original Posts show up, but not B's replies
>* Feed content is not censored, filtered, prioritized by select authors nor following size. For now, content is only sortable in reverse chronology 


## Live:
>**PERSISTENT DATA - PostGres:**
Heroku doesn't support persistent data with SQLlite, which drove me towards PostGres. This marks my first PostGres installation ever.



## New technical achievements:
>**PERSISTENT DATA - PostGres:**
Heroku doesn't support persistent data with SQLlite, which drove me towards PostGres. This marks my first PostGres installation ever.

>**MULTIPLE DEVICES:**
Had to install and configure PostGres on a 2nd machine, creating a 2nd database altogether and figuring out git updates

## Potential improvements:
>**NESTED REPLIES:**<br>
Think of Reddit.com's reply structure<br>

>**DOWNVOTING:**
  
>**NESTED REPLIES:**<br>
Think of Reddit.com's reply structure<br>

>**RECOMMENDATION ENGINE:**<br>
Feed content would be filtered and prioritized based off a staff-determined scoring system. A further advancement would allow users to customize how this recommendation engine thinks i.e. would it focus on the speaker more than the message content? The topic more than the recency?