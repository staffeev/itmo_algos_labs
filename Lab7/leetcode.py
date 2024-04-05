from collections import defaultdict


class Solution:

    def find(self, s, wlen, base, mod):
        d = defaultdict(int)
        hs = 0
        for i in range(wlen):
            hs = (hs * base + s[i]) % mod
        d[hs] += 1
        pw = base ** (wlen - 1) % mod
        for i in range(1, len(s) - wlen + 1):
            hs = (base * (hs - s[i - 1] * pw) + s[i + wlen - 1]) % mod
            d[hs] += 1
            if d[hs] == 2:
                return True, (i, i + wlen)
        return False, (None, None)

    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        ords = [ord(s[i]) - ord("a") for i in range(n)]
        lb, rb = 0, n
        last_ix = None
        while lb + 1 < rb:
            mid = (lb + rb) // 2
            found, ix = self.find(ords, mid, 31, 288712734377)
            if found:
                lb = mid
                last_ix = ix
            else:
                rb = mid
        if last_ix is None:
            return ""
        return s[last_ix[0]:last_ix[1]]



if __name__ == "__main__":
    tt = "unuoqslvgaekunapeaapsxbodakcrapmmfuxoowlysenyiygzhawbfbuxlswtxzzhlspfgzckzuoxizijrluvndcpnknsvrnfulksqqxdznfjgjlocozuolroealyhhwrzcsuzgcsekkqmwlnylsscpmynjchwvpwebwkraudfqboeqmxhghekcstrcozldbwyniwqmyrbkzwvknulehzxwckwohlmjvlqyexvzzlptbnnbctywyezcssubmiukcsixmnapgttmlfwtwnmxqgsobqsnxucwrszxcuprnlxjteytwqzridgtgkkbsekeytuxslavhebbpjewdwlhchtzwohqkojiqneahxacutymteoyloottnsmmrphngclortfvudoeckxkjqatxqmvboumxmdrxoxpyprkwvfpviqkbhsjdeosxdbzzfsomrxojkokofrrdoavhjufyayisibcgngqprircpcjyvynhzmrtyynfgfgeomscywbcvmlhcmyesuxwurmpdxhddyfnumgkvphmtqzrbsbjeliyrqfswrchkurvqtsmzchjfvotdmueabpllagtfvefssmgevrzydftuvxqdbdrpysifoxgvlkljhkiksoxfndxayrsaxeoefmimnqfeerggwxsbyarfvfwvrmtwjainqposafhwysxaaegzeewhyrsfnduqihpwipeewnubscqpvjekikyiwmpwynydbnvylqydgiwsenvulkknlbuqpwhxqclrnuvdwqpxkksyewsklffwtggbmxnttvnjbiqjdoezffmmighfdcirjakacncwckjqwqsjxsbsxbaeaagmnybxpwvucyskfkydlkxdlfmodygcxzimmhdgmwwqxrflldkwvyqlfwasxxoetlgtopmqnfkfvkshkrikfcvdrguxciupphxyssowakrnsiutntlliedxnqkldzfkqefgvyaargpqbknlmlbejkuupolrhapowrgciyteeeulpldvlqkklwsxtvcmxjozbfqgmslutnkspfoaeylxufmuropnafrjveufqymddcrzvbdkhghzvbjzxyuibkemslbsluzwnduiutluergimcjsziusnqhyazuhskekblpoexmurndswlwxwieujdyilfntaaphwvnauvwmihlfphfpxzkwinxitiqxamjqxtdxswgxfmsfuqwtqqnzracsoerlrntgyypdroiuqtiawxeogqcrxxbjmgkqrlrbgeglkamqfvgaiipuxcvllcujnnlfzidrvzowaupaucbxzwzhueqqdphpmsdszdtcycrmiwyhslbvknlxhfgpcbotvarakaymjgfydzfmnxwausfhdxulmxhvzgbswfdwrtitwyibwfnpsekmymsglzpiyrhnuaatmqkjqhcwycnaxjbxqgprgoesjnupyfhbyounmbwgjfplslyudxyaxuspyxjcuorzxcryiuwlgprpurjdxozsalkbjcjatnxstbxinrokiufjldyuyngkiobomuemplhziwaapevhrluxohodizmmqznpbggcaqfgobgpvytmbpdmrrcbzbgrppmlmigghuzrdfhwhksgmmnjnbglrrckwbdstsjdjxaeopxawedvszchktinhceceauookzcwbdkbglzkedrjuqhrnaxluttcjbbdmqimlgppvuvmjqipkcjvyzhingwymthqrpguhvlcjqrstczkdvdrwwtwdrakmbxzjfsszpziurglmpsyllgxtbewoftnhvzmtygsvbnwhltwqszqdopzxbwyrdyrpffnilfdxtlofyicjshyrpncsqndubqkgkgrtbybulwegugcvfqhpfnvvccocolfpiyojgoranoyegkpitmfkmdkyihdqscwykyhgkyljypjobeijjvdpjglbkefxtsmyyytluqpvdcsgrtvsamzupdjyzqtcvpoquialxzaeerxtqkitsapniklylrztgclbxyzzrkanhucwdccdvafyirulajxbmeyaoqtqpprkohdddzdxtiwwctcevneriqahvrgyqvyrwfcvvqbhxmiajqkwhztepimveqisonqccfgwnhpkkqsqlmqqszwjxcpmyzldhjmriayuxpfosdtmhvtncuboiggyroxgwlbybievmdwaverpetzrmeogojuyipkwsibihuhzxjnwugjpwonfsbwaxfcqveyipwkhkzsfarvxrdlxvoiduextlcnnwuaiishdbfnxvfzkqfbqynfznbqijfkamnhlwcmkysbotlebtyfkoptfignbwxfldmbebmtyoggfvbyyygbibfhgfrdtwptwihjndlxmtdkntxtfjwstbmukwlwkzecogozerskubaxjqtliwpgyfwvkqqagmwmnfvuoujlelopdbfqyjnemaibfmgfhqzoptcolufrgafmwkzlxaudgvkhicwjdyomiqgoapvhyakslmhnznivjulyyqusxolkmfyskcfgshotfdjbtmflvtagraeazawnbtcquiivziijjporrsuytdkayjtnexvwtoswqmncbvwsxcaowrjmqdtyzqdjrqbmnaqqlkbdsrweeofeztqlgijzsriayrlknxcinibqqguxztuikzetcwipuchwukczxunuoqslvgaekunapeaapsxbodakcrapmmfuxoowlysenyiygzhawbfbuxlswtxzzhlspfgzckzuoxizijrluvndcpnknsvrnfulksqqxdznfjgjlocozuolroealyhhwrzcsuzgcsekkqmwlnylsscpmynjchwvpwebwkraudfqboeqmxhghekcstrcozldbwyniwqmyrbkzwvknulehzxwckwohlmjvlqyexvzzlptbnnbctywyezcssubmiukcsixmnapgttmlfwtwnmxqgsobqsnxucwrszxcuprnlxjteytwqzridgtgkkbsekeytuxslavhebbpjewdwlhchtzwohqkojiqneahxacutymteoyloottnsmmrphngclortfvudoeckxkjqatxqmvboumxmdrxoxpyprkwvfpviqkbhsjdeosxdbzzfsomrxojkokofrrdoavhjufyayisibcgngqprircpcjyvynhzmrtyynfgfgeomscywbcvmlhcmyesuxwurmpdxhddyfnumgkvphmtqzrbsbjeliyrqfswrchkurvqtsmzchjfvotdmueabpllagtfvefssmgevrzydftuvxqdbdrpysifoxgvlkljhkiksoxfndxayrsaxeoefmimnqfeerggwxsbyarfvfwvrmtwjainqposafhwysxaaegzeewhyrsfnduqihpwipeewnubscqpvjekikyiwmpwynydbnvylqydgiwsenvulkknlbuqpwhxqclrnuvdwqpxkksyewsklffwtggbmxnttvnjbiqjdoezffmmighfdcirjakacncwckjqwqsjxsbsxbaeaagmnybxpwvucyskfkydlkxdlfmodygcxzimmhdgmwwqxrflldkwvyqlfwasxxoetlgtopmqnfkfvkshkrikfcvdrguxciupphxyssowakrnsiutntlliedxnqkldzfkqefgvyaargpqbknlmlbejkuupolrhapowrgciyteeeulpldvlqkklwsxtvcmxjozbfqgmslutnkspfoaeylxufmuropnafrjveufqymddcrzvbdkhghzvbjzxyuibkemslbsluzwnduiutluergimcjsziusnqhyazuhskekblpoexmurndswlwxwieujdyilfntaaphwvnauvwmihlfphfpxzkwinxitiqxamjqxtdxswgxfmsfuqwtqqnzracsoerlrntgyypdroiuqtiawxeogqcrxxbjmgkqrlrbgeglkamqfvgaiipuxcvllcujnnlfzidrvzowaupaucbxzwzhueqqdphpmsdszdtcycrmiwyhslbvknlxhfgpcbotvarakaymjgfydzfmnxwausfhdxulmxhvzgbswfdwrtitwyibwfnpsekmymsglzpiyrhnuaatmqkjqhcwycnaxjbxqgprgoesjnupyfhbyounmbwgjfplslyudxyaxuspyxjcuorzxcryiuwlgprpurjdxozsalkbjcjatnxstbxinrokiufjldyuyngkiobomuemplhziwaapevhrluxohodizmmqznpbggcaqfgobgpvytmbpdmrrcbzbgrppmlmigghuzrdfhwhksgmmnjnbglrrckwbdstsjdjxaeopxawedvszchktinhceceauookzcwbdkbglzkedrjuqhrnaxluttcjbbdmqimlgppvuvmjqipkcjvyzhingwymthqrpguhvlcjqrstczkdvdrwwtwdrakmbxzjfsszpziurglmpsyllgxtbewoftnhvzmtygsvbnwhltwqszqdopzxbwyrdyrpffnilfdxtlofyicjshyrpncsqndubqkgkgrtbybulwegugcvfqhpfnvvccocolfpiyojgoranoyegkpitmfkmdkyihdqscwykyhgkyljypjobeijjvdpjglbkefxtsmyyytluqpvdcsgrtvsamzupdjyzqtcvpoquialxzaeerxtqkitsapniklylrztgclbxyzzrkanhucwdccdvafyirulajxbmeyaoqtqpprkohdddzdxtiwwctcevneriqahvrgyqvyrwfcvvqbhxmiajqkwhztepimveqisonqccfgwnhpkkqsqlmqqszwjxcpmyzldhjmriayuxpfosdtmhvtncuboiggyroxgwlbybievmdwaverpetzrmeogojuyipkwsibihuhzxjnwugjpwonfsbwaxfcqveyipwkhkzsfarvxrdlxvoiduextlcnnwuaiishdbfnxvfzkqfbqynfznbqijfkamnhlwcmkysbotlebtyfkoptfignbwxfldmbebmtyoggfvbyyygbibfhgfrdtwptwihjndlxmtdkntxtfjwstbmukwlwkzecogozerskubaxjqtliwpgyfwvkqqagmwmnfvuoujlelopdbfqyjnemaibfmgfhqzoptcolufrgafmwkzlxaudgvkhicwjdyomiqgoapvhyakslmhnznivjulyyqusxolkmfyskcfgshotfdjbtmflvtagraeazawnbtcquiivziijjporrsuytdkayjtnexvwtoswqmncbvwsxcaowrjmqdtyzqdjrqbmnaqqlkbdsrweeofeztqlgijzsriayrlknxcinibqqguxztuikzetcwipuchwukczx"
    # tt = "banana"
    s = Solution()
    print(s.longestDupSubstring(tt))
    # 1000015279
    # print(tt.count("mrpkh"))
    # print(tt.count("hnvyavlhqnapuherhxqlzyeyswnfdrixkagkhbmovprtrqiojnyrbaozzenamujynxwymymqcsqptyypptoqjutirxoyychearrbtlkswiqwkrddwiuchjlfvattexashrkicdruj"))