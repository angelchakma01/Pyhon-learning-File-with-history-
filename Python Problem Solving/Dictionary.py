
# 💻 শুধু .update() মেথডের প্রblems:
# ১. একটি নির্দিষ্ট ভ্যালু পরিবর্তন করা (Basic Update)
# আপনার কাছে একটি ডিকশনারি আছে যেখানে কোর্সের ফি ভুল দেওয়া আছে:

# Python
# course = {"title": "Python Basics", "fee": 5000}
# এখন .update() মেথড ব্যবহার করে fee-এর মান পরিবর্তন করে free (অথবা 0) করুন।


course ={"Title":"Python Basics","Fee":5000}
course.update({"Fee":0})

print(course["Fee"])

# ২. একসাথে একাধিক তথ্য আপডেট ও নতুন তথ্য যোগ করা
# নিচের ডিকশনারিটিতে ইউজারের লোকেশন ভুল আছে এবং তার ফোন নম্বরটি এখনো যুক্ত করা হয়নি:

# Python
# user_profile = {"name": "Angel", "location": "Sylhet"}
# .update() মেথড ব্যবহার করে এক লাইনে দুটি কাজ করুন:

# location পরিবর্তন করে "Dhaka" করুন।

# নতুন একটি কী (Key) "phone": "017XXXXXXXX" যোগ করুন।
user_profile = {
    "Name":"Angel",
    "location":"Sylhet"
}