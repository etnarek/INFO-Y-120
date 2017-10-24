import  email
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

#Retrieve mails from TR or TT folders
def get_mails(folder, size):
    mails = []
    i = 1
    if folder == "TR":
        file_type = "TRAIN_"
    elif folder == "TT":
        file_type = "TEST_"
    else:
        file_type = ""
    while i < size+1:
        filename = folder + "/" + file_type + str(i) + ".eml"
        with open(filename, "rb") as file:
            mails.append(email.message_from_binary_file(file))
        i = i +1
        file.close()
    return mails

#Retrieve the values 0 or 1 from the training mails    
def get_train_label(filename):
    labels = []
    with open (filename, "r") as file:
        next(file)
        for line in file:
            if line[1] == ",":
                labels.append(line[2])
            elif line[2] == ",":
                labels.append(line[3])
            elif line[3] == ",":
                labels.append(line[4])
            elif line[4] == ",":
                labels.append(line[5])
    return labels

#Extract payload from a mail list  
def extract_payload(mails):
    payloads = []
    for i in mails:
        payload = i.get_payload()
        if type(payload) == type(list()):
            payload = payload[0]
        if type(payload) == type(i):
            payload = payload.get_payload()
        if type(payload) != type('') :
            payload = str(payload)
        payloads.append(payload)
    return payloads

#Extract the payloads and the values (0 or 1)         
train = get_mails("TR", 2500)
test = get_mails("TT", 1827)
train_payload = extract_payload(train)
test_payload = extract_payload(test)
train_label = get_train_label("spam-mail.tr.label")

#WTF from tuto
count_vect = CountVectorizer(stop_words = "english", strip_accents="unicode").fit(train_payload, test_payload)
X_train_counts = count_vect.transform(train_payload)
clf = MultinomialNB().fit(X_train_counts, train_label)
X_test_counts = count_vect.transform(test_payload)
predicted = clf.predict(X_test_counts)

#Results
with open("results.txt", "w") as result:
    mail_number = 1
    for prediction in predicted:
        result.write(str(mail_number) + "," + str(prediction) + "\n")
        mail_number = mail_number + 1
