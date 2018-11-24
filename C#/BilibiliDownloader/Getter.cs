using System;
using System.Text;
using System.Net;
using System.IO;
using System.IO.Compression;

namespace BilibiliGetter
{
    class Getter
    {
        public static string GetHtmlWithUtf(string url)
        {
            if (!(url.Contains("http://") || url.Contains("https://")))
            {
                url = "http://" + url;
            }
            HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);
            //Set Cookie to let bilibili.com set true message
            req.Headers.Add(HttpRequestHeader.Cookie, "buvid3=00000000-0000-0000-0000-000000000;im_notify_type_1=0");
            req.ContentType = "text/xml";

            string sHTML = "";
            using (HttpWebResponse response = (HttpWebResponse)req.GetResponse())
            {
                using (GZipStream stream = new GZipStream(response.GetResponseStream(), CompressionMode.Decompress))
                {
                    using (StreamReader reader = new StreamReader(stream, Encoding.UTF8))
                    {
                        sHTML = reader.ReadToEnd();
                    }
                }
            }
            return sHTML;
        }
        static void Main(string[] args)
        {
            if (!(args.Length == 0))
            {
                Console.WriteLine(GetHtmlWithUtf(args[0]));
            }
            else
            {
                Console.WriteLine("只能获取Bilibili的视频页的HTML");
                Console.WriteLine(GetHtmlWithUtf(Console.ReadLine()));
            }
        }
    }
}
