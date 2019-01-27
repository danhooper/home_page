package com.danhooper.homepage.controller;

import com.danhooper.homepage.FeedConfig;
import com.danhooper.homepage.model.RssArticle;
import com.danhooper.homepage.model.RssFeed;
import com.danhooper.homepage.service.RssArticleFetcher;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;

@RestController
public class RssArticleController {
    @Autowired
    FeedConfig feedConfig;

    @RequestMapping("/rss/{id}/article")
    public List<RssArticle> getArticles(@PathVariable("id") int id) {
        RssArticleFetcher fetcher = new RssArticleFetcher();
        return fetcher.getArticles(feedConfig.getFeeds().get(id));
    }
}