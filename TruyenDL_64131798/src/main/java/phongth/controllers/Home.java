package phongth.controllers;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;


@Controller
public class Home{
	@GetMapping("/")
	public String getMethodName(@RequestParam(name = "param", required = false, defaultValue = "defaultValue") String param) {
	    System.out.println("Received param: " + param);
	    return "index";
	}

}