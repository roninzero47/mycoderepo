//import java.util.Date;
import java.awt.*;
class HelloWorld{
    public static void main(String[] args) {
        //Date now = new Date();
        Point point1 = new Point(2,1);
        Point point2 = point1;
        point1.x = 4;
        System.out.println(point2);
    }
}