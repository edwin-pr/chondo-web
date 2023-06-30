# views.py

from django.shortcuts import render
import nfc

def read_nfc(request):
    # Create an NFC reader instance
    clf = nfc.ContactlessFrontend()

    # Connect to the first available NFC reader
    clf.open('usb:')

    # Read NFC tags
    while True:
        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        if tag.ndef:
            # Extract the data from the NFC tag
            data = tag.ndef.message.pretty()
            # Process and store the data in the database
            # ... (your code here)
            break

    # Close the NFC reader
    clf.close()

    return render(request, 'read_nfc.html', {'data': data})
