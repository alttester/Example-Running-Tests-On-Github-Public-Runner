
// For more info on the setup, check out our docs https://alttester.com/docs/sdk/latest/pages/get-started.html#write-and-execute-first-test-for-your-app  
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import com.google.gson.JsonElement;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParser;
import com.alttester.Commands.FindObject.*;
import com.alttester.Commands.UnityCommand.*;
import com.alttester.Commands.InputActions.*;
import com.alttester.UnityStruct.*;
import com.alttester.Commands.ObjectCommand.*;
import com.alttester.position.Vector2;
import com.alttester.AltObject;
import com.alttester.AltDriver;

public class MyTests {
        private static AltDriver altDriver;
        public String textscreen__titlePath = "/RuntimePanelSettings/FlexboxDemo-container/background/text-screen__container/text-screen__header/text-screen__title";
        public String textscreen__footerPath = "/RuntimePanelSettings/FlexboxDemo-container/background/text-screen__container/text-screen__footer";

        @BeforeAll
        public static void oneTimeSetUp() throws Exception {
                altDriver = new AltDriver("127.0.0.1", 13000, true, 60, "__default__");
                // You might want to load the scene here
                // altDriver.loadScene(new AltLoadSceneParams.Builder("FlexboxDemo").build());
        }

        @AfterAll
        public static void oneTimeTearDown() throws Exception {
                altDriver.stop();
        }

        @Test
        public void Test() throws InterruptedException {
                altDriver.loadScene(new AltLoadSceneParams.Builder("FlexboxDemo").loadSingle(true).build());
                AltObject textscreen__title = altDriver.waitForObject(new AltWaitForObjectsParams.Builder(
                                new AltFindObjectsParams.Builder(AltDriver.By.PATH, textscreen__titlePath).build())
                                .withTimeout(20).build());
                textscreen__title.waitForVisualElementProperty(
                                new AltWaitForVisualElementPropertyParams.Builder("text").withTimeout(20).build(),
                                new GsonBuilder().serializeNulls().create().toJsonTree("Flexbox layout"), true,
                                JsonElement.class);
                AltObject textscreen__footer = altDriver.waitForObject(new AltWaitForObjectsParams.Builder(
                                new AltFindObjectsParams.Builder(AltDriver.By.PATH, textscreen__footerPath).build())
                                .withTimeout(20).build());
                textscreen__footer.waitForVisualElementProperty(
                                new AltWaitForVisualElementPropertyParams.Builder("height").withTimeout(20).build(),
                                new GsonBuilder().serializeNulls().create().toJsonTree("85.8688354"), true,
                                JsonElement.class);
                textscreen__footer.waitForVisualElementProperty(
                                new AltWaitForVisualElementPropertyParams.Builder("marginRight").withTimeout(20)
                                                .build(),
                                new GsonBuilder().serializeNulls().create().toJsonTree("0"), true, JsonElement.class);
                textscreen__footer.waitForVisualElementProperty(
                                new AltWaitForVisualElementPropertyParams.Builder("minWidth").withTimeout(20).build(),
                                new GsonBuilder().serializeNulls().create().toJsonTree(
                                                JsonParser.parseString("{  \"value\": 0.0,  \"keyword\": 2}")),
                                true, JsonElement.class);
                textscreen__footer.waitForVisualElementProperty(
                                new AltWaitForVisualElementPropertyParams.Builder("rotate").withTimeout(20).build(),
                                new GsonBuilder().serializeNulls().create().toJsonTree(JsonParser
                                                .parseString("{  \"angle\": {    \"value\": 0.0,    \"unit\": 0  }}")),
                                true, JsonElement.class);
                textscreen__footer.waitForVisualElementProperty(
                                new AltWaitForVisualElementPropertyParams.Builder("transitionDuration").withTimeout(20)
                                                .build(),
                                new GsonBuilder().serializeNulls().create().toJsonTree(
                                                JsonParser.parseString("[  {    \"value\": 0.0,    \"unit\": 0  }]")),
                                true, JsonElement.class);
                textscreen__footer.waitForVisualElementProperty(
                                new AltWaitForVisualElementPropertyParams.Builder("transitionProperty").withTimeout(20)
                                                .build(),
                                new GsonBuilder().serializeNulls().create()
                                                .toJsonTree(JsonParser.parseString("[  {}]")),
                                true, JsonElement.class);
                textscreen__footer.waitForVisualElementProperty(
                                new AltWaitForVisualElementPropertyParams.Builder("transitionTimingFunction")
                                                .withTimeout(20).build(),
                                new GsonBuilder().serializeNulls().create()
                                                .toJsonTree(JsonParser.parseString("[  {    \"mode\": 0  }]")),
                                true, JsonElement.class);
        }
}
