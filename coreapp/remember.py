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
#@register.filter            custom filter बनाउन प्रयोग हुन्छ। ntr {{ student.DOB|nepali_date }} kam grdain--------->
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


#===========nepali date click grda automatically english ma convert hune========
#<script src="https://unpkg.com/nepali-date-converter/dist/nepali-date-converter.min.js"></script>


#9).<script>
#document.addEventListener("DOMContentLoaded", function () {
#            let mode = "english";
#            const inputs = document.querySelectorAll(".lang-input");  ---->.lang-input class भएका सबै input elements select गर्छ।
#            const bsInput = document.getElementById("bs-date");
#            const adOutput = document.getElementById("ad-date");
#            // ==========================================
#            // YOUR CUSTOM BS -> AD MATHEMATICAL CONVERTER
#            // ==========================================
#            bsInput.addEventListener("input", function () {  ------>जब user ले typing गर्छ (input event), यो function चल्छ
#                const value = this.value.trim();  ---->this.value=input box मा लेखिएको text ----->trim()=अगाडि/पछाडिको खाली space हटाउँछ
#                const parts = value.split("-");   --------> ["2081", "05", "10"]yesto ma lagne
#                // Keep output empty while the user is still typing the full date layout
#                if (parts.length !== 3 || parts[2] === "") {
#                    adOutput.value = "";
#                    return;
#                }
#                const bsYear = parseInt(parts[0]);
#                const bsMonth = parseInt(parts[1]);
#                const bsDay = parseInt(parts[2]);
#                if (isNaN(bsYear) || isNaN(bsMonth) || isNaN(bsDay)) { -------->date valid छ कि छैन check गर्छ
#                    adOutput.value = "Invalid input";
#                    return;
#                }
#                // Utilizing your custom conversion rules directly
#                let adYear = bsYear - 56;
#                let adMonth = bsMonth - 8;
#                let adDay = bsDay;
#                if (adMonth <= 0) {
#                    adYear -= 1;
#                    adMonth += 12;
#                }
#                const adDate = new Date(adYear, adMonth - 1, adDay);
#                // Format output cleanly into standard YYYY-MM-DD format
#                if (!isNaN(adDate.getTime())) {
#                    const yyyy = adDate.getFullYear();    --------->year निकाल्छ
#                    const mm = String(adDate.getMonth() + 1).padStart(2, '0');      ------>+1 किनभने JS month 0-based हुन्छ
#                    const dd = String(adDate.getDate()).padStart(2, '0');     ------>day निकाल्छ
#                    adOutput.value = `${yyyy}-${mm}-${dd}`;
#                } else {
#                    adOutput.value = "Invalid Date Calculation";       ------->यदि date wrong भयो भने message देखाउँछ।
#                }
#            });
#</script>


#***********------ english letter convetred in nepali letter *********** --------------->

#------column ko mathi rakhne ----------->
#1). <div class="d-flex justify-content-end mb-3">            --------->english lai switch grer nepali ma lagne 
#    <button type="button" id="btnEnglish" class="btn btn-secondary me-2">
#        English
#    </button>
#    <button type="button" id="btnNepali" class="btn btn-success">    ------->english lai switch grer nepali ma lagne 
#        नेपाली
#    </button>
#</div>


#2). input-------> class="form-control lang-input"    ------->lang-input भएको सबै input मा language conversion लागू हुन्छ।
#3).<script>
#        document.addEventListener("DOMContentLoaded", function () {
#            let mode = "english";
#            // ENGLISH BUTTON
#            document.getElementById("btnEnglish").addEventListener("click", function () {
#                mode = "english";
#                // FORM TITLE
#                document.getElementById("formTitle").innerText = "Add Student Form";
#                // LABELS
#                document.getElementById("lblName").innerText = "Full Name";
#                document.getElementById("lblAge").innerText = "Age";
#                document.getElementById("lblAddress").innerText = "Address";
#                document.getElementById("lblEmail").innerText = "Email";
#                document.getElementById("lblDOB").innerText = "DOB";
#                document.getElementById("lblContact").innerText = "Contact";
#                document.getElementById("lblImage").innerText = "Image";
#                document.getElementById("lblVideo").innerText = "Video";
#                document.getElementById("lblPDF").innerText = "PDF";
#                // BUTTON
#                document.getElementById("submitBtn").innerText = "Submit";#
#            });#
#            // NEPALI BUTTON
#            document.getElementById("btnNepali").addEventListener("click", function () {#
#                mode = "nepali";
#                // FORM TITLE
#                document.getElementById("formTitle").innerText = "विद्यार्थी फारम";#
#                // LABELS
#                document.getElementById("lblName").innerText = "पूरा नाम";
#                document.getElementById("lblAge").innerText = "उमेर";
#                document.getElementById("lblAddress").innerText = "ठेगाना";
#                document.getElementById("lblEmail").innerText = "इमेल";
#                document.getElementById("lblDOB").innerText = "जन्म मिति";
#                document.getElementById("lblContact").innerText = "सम्पर्क";
#                document.getElementById("lblImage").innerText = "तस्वीर";
#                document.getElementById("lblVideo").innerText = "भिडियो";
#                document.getElementById("lblPDF").innerText = "पीडीएफ";#
#                // BUTTON
#                document.getElementById("submitBtn").innerText = "पेश गर्नुहोस्";#
#            });#
#        });
#    </script>


#============nepali converter================
#<script>
#// =========================
#            // NEPALI CONVERTER (basic)
#            // =========================
#            function toNepali(text) {
#                return text
#                    .replace(/a/g, "अ")
#                    .replace(/b/g, "ब")
#                    .replace(/c/g, "क")
#                    .replace(/d/g, "द")
#                    .replace(/e/g, "ए")
#                    .replace(/g/g, "ग")
#                    .replace(/h/g, "ह")
#                    .replace(/i/g, "इ")
#                    .replace(/k/g, "क")
#                    .replace(/l/g, "ल")
#                    .replace(/m/g, "म")
#                    .replace(/o/g, "ओ")
#                    .replace(/p/g, "प")
#                    .replace(/r/g, "र")
#                    .replace(/s/g, "स")
#                    .replace(/t/g, "त")
#                    .replace(/u/g, "उ")
#                    .replace(/y/g, "य");
#            }
# </script>


