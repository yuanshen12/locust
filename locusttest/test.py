from locust import HttpLocust, TaskSet, task


class BlogDemo(TaskSet):
    @task(1)
    def open_blog(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Window NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        r = self.client.get("/d?sid=52&cat=31&page=1&rows=500", headers=header, verify=False)
        print(r.status_code)
        assert r.status_code == 200


class WebsitUser(HttpLocust):
    task_set = BlogDemo
    min_wait = 3000
    max_wait = 6000


if __name__ == '__main__':
    import os

    os.system('locust -f test.py --host=https://m.jiuxiao2.cn')
