using AltTester.AltTesterUnitySDK.Driver;

namespace SimpleTest;

public class Tests
{
    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void Test1()
    {
        AltDriver driver = new AltDriver();
        Assert.Pass();
    }
}