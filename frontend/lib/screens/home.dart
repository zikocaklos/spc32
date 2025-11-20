import 'package:flutter/material.dart';
import '../services/api.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  double distance = 0;
  double light = 0;

  bool redLed = false;
  bool yellowLed = false;
  bool greenLed = false;

  @override
  void initState() {
    super.initState();
    loadData();
    Future.delayed(const Duration(milliseconds: 200), refreshLoop);
  }

  void refreshLoop() async {
    while (mounted) {
      await loadData();
      await Future.delayed(const Duration(seconds: 2));
    }
  }

  Future loadData() async {
    try {
      final data = await ApiService.getData();

      setState(() {
        distance = data["sensor"]["distance"] ?? 0;
        light = data["sensor"]["light"] ?? 0;

        redLed = data["leds"]["red"] == 1;
        yellowLed = data["leds"]["yellow"] == 1;
        greenLed = data["leds"]["green"] == 1;
      });
    } catch (e) {
      debugPrint("Error obteniendo datos: $e");
    }
  }

  Future updateLeds() async {
    await ApiService.setLeds(
      redLed ? 1 : 0,
      yellowLed ? 1 : 0,
      greenLed ? 1 : 0,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("ESP32 Control Panel"),
        backgroundColor: Colors.deepPurple,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [

            const Text(
              "📡 Datos del ESP32",
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),

            const SizedBox(height: 15),

            Text("Distancia: ${distance.toStringAsFixed(2)} cm",
                style: const TextStyle(fontSize: 18)),

            Text("Luz: $light",
                style: const TextStyle(fontSize: 18)),

            const Divider(height: 40),

            const Text(
              "💡 Control Manual de LEDs",
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),

            SwitchListTile(
              title: const Text("LED Rojo"),
              value: redLed,
              activeColor: Colors.red,
              onChanged: (v) {
                setState(() => redLed = v);
                updateLeds();
              },
            ),

            SwitchListTile(
              title: const Text("LED Amarillo"),
              value: yellowLed,
              activeColor: Colors.amber,
              onChanged: (v) {
                setState(() => yellowLed = v);
                updateLeds();
              },
            ),

            SwitchListTile(
              title: const Text("LED Verde"),
              value: greenLed,
              activeColor: Colors.green,
              onChanged: (v) {
                setState(() => greenLed = v);
                updateLeds();
              },
            ),
          ],
        ),
      ),
    );
  }
}
