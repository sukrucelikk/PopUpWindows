from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Test Notification",
                   "Hello Sukru",
                   duration=10)
