import imp
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from caps.views import index,create_caps,cart,create_order,most_viewed,best_seller,latest_arrivals,about,show_caps

# Create your tests here.
class Testurls(SimpleTestCase):
    
    def test_case_index_urls(self):
        urls = reverse('home')
        self.assertEquals(resolve(urls).func,index)
        
    def test_case_about_urls(self):
        urls = reverse('about')
        self.assertEquals(resolve(urls).func,about)
        
    def test_case_create_caps_urls(self):
        urls = reverse('create_caps')
        self.assertEquals(resolve(urls).func,create_caps)
        
        
    def test_case_most_viewed_urls(self):
        urls = reverse('most_viewed')
        self.assertEquals(resolve(urls).func,most_viewed)
        
    def test_case_latest_arrivals_urls(self):
        urls = reverse('latest_arrivals')
        self.assertEquals(resolve(urls).func,latest_arrivals)
        
    def test_case_best_seller_urls(self):
        urls = reverse('best_seller')
        self.assertEquals(resolve(urls).func,best_seller)
        
    def test_case_show_caps_urls(self):
        urls = reverse('show_caps')
        self.assertEquals(resolve(urls).func,show_caps)
