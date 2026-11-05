# Source for every Insights article. Add a new dict to ARTICLES (newest first) and run:
#   python3 tools/build_insights.py
# Copy rules: no em dashes, Title Case headings, "investment" never "cost", examples rotate industries.
# Body blocks: ("p", text) ("h2", text) ("steps", [(title, text), ...]) ("example", text) ("figure", svg_key, caption)

ARTICLES = [
{
 "slug": "what-should-a-small-business-fix-first",
 "tag": "Operations",
 "date": "2026-11-04",
 "title": "What Should a Small Business Fix First?",
 "description": "Fix the problem that happens most often and that customers can feel. A simple two-week tally and one grid make the answer obvious.",
 "answer": "Fix the problem that happens most often and that your customers can feel. Not the loudest problem, and not the newest one. A two-week tally of what keeps going wrong usually makes the answer obvious.",
 "body": [
  ("h2", "Why the Loudest Problem Is Rarely the Right One"),
  ("p", "Every owner has a list. The website feels dated, a team member keeps missing details, the software is clunky, reviews could be better. When everything feels urgent, the problem that gets fixed is usually the one that caused the most stress this week."),
  ("p", "That is a feeling, not a pattern. The problem worth fixing first is the one that keeps repeating and keeps touching customers, because every repeat quietly costs you trust, time or a sale."),
  ("h2", "Two Questions Sort the Whole List"),
  ("p", "Ask two things about every problem on your list. How often does it happen? And how close is it to the customer? Put the answers on a simple grid and your priorities sort themselves."),
  ("figure", "grid", "The Fix First grid. Problems that happen often and that customers feel go to the top of the list."),
  ("p", "Problems in the top right are your Fix First list. Frequent but internal problems get scheduled. Rare problems customers feel get watched. Rare internal problems can usually be let go for now."),
  ("example", "A gift boutique was set on redesigning its website. A two-week tally showed the real repeat problem was online orders shipping a day late, which showed up in reviews and support emails every week. Fixing the packing routine did more for sales than the redesign would have."),
  ("h2", "The Move"),
  ("steps", [
    ("Keep a Two-Week Tally", "Every time something goes wrong, write one line: what happened and who noticed. Ask your team to add to it. Two weeks is enough to see what repeats."),
    ("Place Each Problem on the Grid", "Count how often each one showed up, then mark whether customers felt it. Be honest about the second part. If a customer waited, called or complained, they felt it."),
    ("Fix One Thing Completely", "Pick the single problem furthest into the top right and fix it all the way before starting the next. Half-fixed problems come back."),
  ]),
 ],
 "check": [
  "Could you name the problem that happened most often last month?",
  "Have you fixed something recently that customers never noticed?",
  "Does your team agree on what the biggest repeat problem is?",
 ],
 "check_note": "If you hesitated on any of these, a two-week tally will tell you more than another planning meeting.",
 "pattern": "The problem that repeats most and touches customers is usually costing more than the one that feels most urgent.",
 "move": "Tally problems for two weeks, sort them by frequency and customer impact, and fix the top one completely.",
},
{
 "slug": "which-customers-are-worth-focusing-on",
 "tag": "Customers",
 "date": "2026-11-04",
 "title": "How Do I Know Which Customers Are Worth Focusing On?",
 "description": "A small group of customers usually drives a large share of revenue and repeat business. Here is how to find them and build around what they have in common.",
 "answer": "In most businesses, a small group of customers brings in a large share of the revenue and the repeat business. Find that group, learn what they have in common, like how they found you and what they bought first, and build more of your business around that path.",
 "body": [
  ("h2", "Why Serving Everyone the Same Spreads You Thin"),
  ("p", "Most small businesses treat every customer the same way: the same messages, the same offers, the same follow-up. It feels fair, but it means your best customers get the same attention as people who will never come back."),
  ("p", "Your best customers are already showing you what works. They found you a certain way, started with a certain purchase and came back for a reason. When you can see that path, you can send more people down it."),
  ("figure", "customers", "An illustration of a common pattern: one small group of customers drives most of the repeat business."),
  ("h2", "How to Find Them Without Fancy Tools"),
  ("p", "Export your customer list from whatever you already use, whether that is a booking system, a point of sale, an online store or even invoices. Then sort it three ways: who spent the most, who came back most often and who bought most recently. The names that show up near the top of all three are your core group."),
  ("example", "A hair salon sorted a year of bookings and found that its most loyal clients almost all started with the same service, a consultation and trim. New clients who started with a single color appointment rarely returned. The salon began promoting the consultation first, and repeat bookings grew."),
  ("h2", "The Move"),
  ("steps", [
    ("Sort Your Customer List", "Rank customers by total spend, number of visits and most recent visit. Mark the people who rank high on all three."),
    ("Find What They Share", "Look at how those customers first found you, what they bought first and when they came back. Look for the answer that repeats."),
    ("Put More Behind That Path", "Promote the first purchase your best customers made, invest in the channel that brought them and follow up the way they responded to."),
  ]),
 ],
 "check": [
  "Could you name your 10 best customers right now?",
  "Do you know how most of them first found you?",
  "Do you treat a first-time customer and a ten-time customer differently?",
 ],
 "check_note": "If any answer was no, your customer list is holding a pattern you have not used yet.",
 "pattern": "A small group of customers drives most of the value, and they usually share the same first step.",
 "move": "Find your core customers, learn the path they took and send more people down it.",
},
{
 "slug": "why-are-sales-flat-when-traffic-is-up",
 "tag": "Growth",
 "date": "2026-11-04",
 "title": "Why Are My Sales Flat When My Traffic Is Up?",
 "description": "When traffic grows and sales do not, the leak is almost always after people arrive. Here is how to find the step where they stop.",
 "answer": "When traffic grows and sales don't, the problem is almost never getting people in the door. It's what happens after they arrive. Somewhere between the first click and the purchase, people are stopping at the same step, and finding that step is the fastest way to turn the traffic you already have into revenue.",
 "body": [
  ("h2", "What Is Usually Happening"),
  ("p", "More visitors feels like progress, so it is natural to keep investing in getting more of them. But if sales stay flat, more traffic just means more people leaving at the same spot. The gap between the two lines is where your growth is hiding."),
  ("figure", "leak", "When traffic climbs and sales stay flat, the space between the lines is the leak."),
  ("p", "The leak usually comes from one of three places. The new visitors are not your buyers, because a channel is bringing browsers instead of customers. The page they land on never clearly asks for the sale or the booking. Or one step adds just enough friction, like a long form, a surprise fee or a hard-to-find button, that people give up."),
  ("example", "A tutoring center doubled its website visits with social media posts, but enrollments stayed the same. The posts sent parents to the homepage, and the enrollment form was three clicks deep. Linking posts straight to a short sign-up page turned the same traffic into new students."),
  ("h2", "The Move"),
  ("steps", [
    ("Walk the Path on Your Phone", "Start where a new customer starts, like a post, an ad or a search, and try to buy or book. Write down every moment you hesitate. Your customers hesitate there too."),
    ("Compare Sources by Buyers, Not Visitors", "Check which channels bring people who actually buy. A source with half the traffic and twice the sales deserves more of your investment."),
    ("Fix the One Step Where Most People Stop", "Choose the biggest drop-off and fix only that. Give it two weeks before you judge the result, so the change has time to show up."),
  ]),
 ],
 "check": [
  "Has your traffic grown over the last few months while sales stayed about the same?",
  "Do you know which channel brings your buyers, not just your visitors?",
  "Can a first-time visitor buy or book from their phone in three taps or fewer?",
 ],
 "check_note": "If you answered yes to the first question and no to either of the others, the leak is likely after the click.",
 "pattern": "Traffic grows, sales stay flat, and visitors keep stopping at the same step.",
 "move": "Find the step where most people stop, fix only that and measure for two weeks.",
},
]
