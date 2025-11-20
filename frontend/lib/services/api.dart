import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // Cambiar luego por tu backend de Render
  static const String baseUrl = "https://TU_BACK_RENDER.onrender.com/api";

  // Obtener datos del ESP32 (distancia, luz, estados de LEDs)
  static Future<Map<String, dynamic>> getData() async {
    final response = await http.get(Uri.parse("$baseUrl/data"));

    return json.decode(response.body);
  }

  // Cambiar estado de los LEDs desde la app
  static Future<bool> setLeds(int red, int yellow, int green) async {
    final response = await http.post(
      Uri.parse("$baseUrl/leds"),
      body: {
        "red": red.toString(),
        "yellow": yellow.toString(),
        "green": green.toString(),
      },
    );

    return response.statusCode == 200;
  }
}
