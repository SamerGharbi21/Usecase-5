import streamlit as st
import base64

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
# Load the GIF and encode it to base64
gif_path = "./image.gif"

with open(gif_path, "rb") as gif_file:
    gif_bytes = gif_file.read()
    encoded_gif = base64.b64encode(gif_bytes).decode("utf-8")

# Embed the GIF in the app and align it to the center
gif_html = f'''
<div style="text-align: center;">
    <img src="data:image/gif;base64,{encoded_gif}" alt="Your Awesome GIF">
</div>
'''
st.write("<h1 style='text-align: right;'>🤔تدور على وظيفه ؟<h1>", unsafe_allow_html=True)
st.write(gif_html, unsafe_allow_html=True)

#st.write("<p style='text-align: right;'>انا طالب مثل اي طالب الحمدلله بشهاده جامعية و اطمح بوظيفه براتب عالي , طبعا سمعت كلام من ناس كثير ان اغلب الوظايف في الرياض و لازم اخرج من البلد عشان الاقي الرواتب العاليه و السلم الوظيفي الممتاز فا قررت ابحث عن هاذي المعلومات<p>", unsafe_allow_html=True)
#st.write("<p style='text-align: right;'>طبعا انا من سكان المدينة المنورة فا قررت ابحث عن مدى توفر الوظايف بمدينتي <p>", unsafe_allow_html=True)

st.image("image1.png" , width=1000)

#st.write("<p style='text-align: right;'>يا الله المدينة فيها اقل من 100 وظيفه؟ و الرايض فيها اكثر من 500 ؟ يعني كلام الناس صح ؟ لازم اخرج من المدينة و اسيب اهلي ؟ <p>", unsafe_allow_html=True)
#st.write("<p style='text-align: right;'> الحمدلله على كل حال طيب في الرياض العالم منفتحه و حريم و رجال يبغو وظايف هناك هذا اذا ما كان الحريم يتوظفو اكثر ايش الحل؟ خليني اشوف اذا في عندهم افضلية للنساء على الرجال ؟ خليني اشيك<p>", unsafe_allow_html=True)

st.image("image2.png" , width=1000)

#st.write("<p style='text-align: right;'>الحمدلله كلنا زي بعض يلا في مشكله انحلت و عدت على خير <p>", unsafe_allow_html=True)
#st.write("<p style='text-align: right;'>يصير باقي اكبر مشكله تواجهني كخريج حديث و تواجه كل واحد حديث تخرج , مشكلة الخبره يا الله يا رب يسرها من عندك , طيب يصير خليني اشيك على رواتب حديثين التخرج هل تستاهل اني اتغرب عشانها و اتبهدل ولا لا <p>", unsafe_allow_html=True)

st.image("image3.png" , width=1000)

#st.write("<p style='text-align: right;'>يلا كلو خير باذن الله الرواتب مهي معقوله صراحه الي حاخذه حصرفه في سكن و اكل و مصاريف شخصيه فا مالها الا اقدم في مكة المكرمة و محافظاتها و الرياض و اصلي الخيره و على الله فاليتوكل المؤمنون <p>", unsafe_allow_html=True)
st.write("<p style='text-align: right;'>بسم الله نقدم ...<p>", unsafe_allow_html=True)
