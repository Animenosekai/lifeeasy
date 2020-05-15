import lifeeasy
lifeeasy.clear()

lifeeasy.display()
display_list = []
lifeeasy.sleep(2)
lifeeasy.display_title('Bienvenue')
lifeeasy.display_body(display_list)
lifeeasy.sleep(2)
display_list = ['Hey']
lifeeasy.display_body(display_list)
lifeeasy.sleep(2)
lifeeasy.display_body(display_list)
lifeeasy.sleep(2)
display_list = ['Hey', 'Hey']
lifeeasy.display_body(display_list)
lifeeasy.sleep(5)
lifeeasy.display_title('Hey')
display_list = ['Hey', 'Hey', 'Hey']
lifeeasy.display_body(display_list)
lifeeasy.sleep(2)

lifeeasy.stop_multi_thread_display()