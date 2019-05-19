Title: Converting Protonmail's VCF files to import to phone
Date: 2019-05-19

# Introduction

[Protonmail](https://protonmail.com) captured my interest a few years ago as privacy-focused
alternative to [Gmail](http://gmail.com).

But one of the problems I faced was my dependence on Google's [Contacts](https://contacts.google.com)
service which kept all of my contacts for me stored on my Android device.
I wanted to move away from this as well. But I also have an animosity towards
having email on my phone.

So without installing Protonmail on my phone, how could I take my contacts stored on Protonmail
and put them on my phone?

Well one obvious way was to export Protonmail's contacts to a [VCF](https://en.wikipedia.org/wiki/VCard) file
and import that onto my phone. Unfortunately, Protonmail's VCF file was using version 4.0,
while my phone (Android version 8) was still stuck on VCF version 2.1. And I wasn't the
only one with issues with converting VCF file format versions:

  * [https://alessandrorossini.org/the-sad-story-of-the-vcard-format-and-its-lack-of-interoperability/](https://alessandrorossini.org/the-sad-story-of-the-vcard-format-and-its-lack-of-interoperability/)
  * [https://android.stackexchange.com/questions/106888/what-vcard-formats-versions-and-encodings-are-supported-for-import](https://android.stackexchange.com/questions/106888/what-vcard-formats-versions-and-encodings-are-supported-for-import)
  * [https://github.com/nextcloud/contacts/issues/492](https://github.com/nextcloud/contacts/issues/492)
  * [https://www.tenorshare.com/icloud-tips/cannot-import-vcf-vcards-into-icloud-how-to-fix.html](https://www.tenorshare.com/icloud-tips/cannot-import-vcf-vcards-into-icloud-how-to-fix.html)

But all of the tools I found went from version 2.1 to something newer. I couldn't find any converters
from a newer version down to an older version.

Protonmail (at the time of this post) uses version 4.0.
So I wrote a converter from version 4.0 (Protonmail) to version 2.1 (what Android still uses).

You can find my converter here: [https://github.com/evandowning/vcf-converter](https://github.com/evandowning/vcf-converter)

So everytime my Protonmail contacts get updated, I export them to a VCF file,
convert it to version 2.1, and transfer it to my Android device to be imported locally.

Enjoy.
