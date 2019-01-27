package com.danhooper.homepage.controller;

import com.danhooper.homepage.FeedConfig;
import com.danhooper.homepage.model.RssArticle;
import com.danhooper.homepage.model.RssFeed;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

@RestController
public class RssController {
    @Autowired FeedConfig feedConfig;

    @RequestMapping("/rss")
    public List<RssFeed> getFeeds() {

        return feedConfig.getFeeds();
//        ArrayList<RssFeed> feeds = new ArrayList<>();
//        try {
//            feeds.add(new RssFeed(0,"ArsTechnica", new URL("http://feeds.arstechnica.com/arstechnica/index?format=xml")));
//        } catch (MalformedURLException e) {
//            e.printStackTrace();
//        }
//        return feeds;
    }
}