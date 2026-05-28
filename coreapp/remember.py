#------------> input nepali time in  this way  ------->   
# 1).-------------> pip install nepali-datetime     --------------> 
#  
# 2). model: ----->   DOB = models.CharField(max_length=100, null=True, blank=True) 
#  
#3). form views :------>  {% load nepali_date %} 

# 4). appname/templatetags/nepali_date.py : ----->create  nepali_date.py 
# 5). nepali_date.py ----->
#from django import template
#import nepali_datetime
#register = template.Library()
#@register.filter
#def nepali(value):   -------------->Template मा यस्तो प्रयोग हुन्छ {{ i.DOB|nepali }}
#    if value:
#        try:
#            bs_date = nepali_datetime.date.from_datetime_date(value)  ----->English date लाई Nepali date मा convert गर्छ।
#            return bs_date.strftime("%Y-%m-%d")   ----------->Nepali date format मा return गर्छ।
#        except:
#            return value
#    return ""            ----------->value खाली भए empty string return गर्छ।

# 6). <td>{{ i.DOB|nepali }}</td>

#  -----------> DOB ---------->
#<input type="text" id="nepawli-date" name="DOB" class="form-control" required>

#------->add form------>above <body>
#--------->css ---------------->  nepali calender design grn
#7).<link rel="stylesheet"href="https://unpkg.com/nepali-date-picker@2.0.2/dist/nepaliDatePicker.min.css">

#----------js-----------> nepali calender chalaun
#8).<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
#<script src="https://unpkg.com/nepali-date-picker@2.0.2/dist/nepaliDatePicker.min.js"></script>

#9).<script>
#$(document).ready(function () {    -------->page पूरा load भएपछि मात्र code चलाउँछ
#    $('#nepali-date').nepaliDatePicker({   ------>id भएको input select गर्छ  ----->त्यो input मा Nepali calendar जोड्छ
#        ndpYear: true,
#        ndpMonth: true ---------->month select option देखाउँछ
#    });
#});
#</script>


#***********------ english letter convetred in nepali letter *********** --------------->
#------column ko mathi rakhne ----------->
#1)<div class="d-flex justify-content-end mb-3">
#    <button type="button" id="btnEnglish" class="btn btn-secondary me-2">
#        English
#    </button>
#    <button type="button" id="btnNepali" class="btn btn-success">
#        नेपाली
#    </button>
#</div>

#2). input-------> class="form-control lang-input"
#3). <!'''<script>
#document.addEventListener("DOMContentLoaded", function () {
#    let mode = "english";
#    document.getElementById("btnEnglish").addEventListener("click", function () {
#        mode = "english";
#        alert("English mode ON");
#    });
#    document.getElementById("btnNepali").addEventListener("click", function () {
#        mode = "nepali";
#        alert("नेपाली mode ON");
#    });
#    function toNepali(text) {
#        return text
#            .replace(/a/g, "अ")
#            .replace(/b/g, "ब")
#            .replace(/c/g, "क")
#            .replace(/d/g, "द")
#            .replace(/e/g, "ए")
#            .replace(/g/g, "ग")
#            .replace(/h/g, "ह")
#            .replace(/i/g, "इ")
#            .replace(/k/g, "क")
#            .replace(/l/g, "ल")
#            .replace(/m/g, "म")
#            .replace(/n/g, "न")
#            .replace(/o/g, "ओ")
#            .replace(/p/g, "प")
#            .replace(/r/g, "र")
#            .replace(/s/g, "स")
#            .replace(/t/g, "त")
#            .replace(/u/g, "उ")
#            .replace(/y/g, "य");
#    }
#    document.querySelectorAll(".lang-input").forEach(input => {
#        input.addEventListener("input", function () {
#            if (mode === "nepali") {
#                this.value = toNepali(this.value);
#            }
#        });
#    });
#});
#</script>