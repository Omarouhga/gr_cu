# Description:
This repository hosts the development of an efficient meal reservation and verification system for residential environments, focusing on user-friendly interfaces and robust functionality.

# Features:
# Class Diagram: 
Illustrates the core entities (Resident, Reservation Agent, Restaurant Manager, Reservation) and their relationships.

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/e70db1b9-b9db-4ca1-919a-fe2a29eb8dfd)

# Deployment Diagram: 
Depicts the architecture, including the Odoo server, databases, web browsers, and embedded systems for RFID verification.

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/df28e82b-8a68-46f3-b6a9-dd2539cc91c7)

# User Roles:
Resident: Activate accounts, reload balances, and make online reservations.
Reservation Agent: Manage resident accounts, especially for those without online reloading options.
Restaurant Manager: Access reservation details for efficient meal planning.
Super Admin: Full system access for administration

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/2a9fddd1-e0b5-46e9-b731-0a8f79e391b4)

# Reservation Agent Interfaces:
Access to resident lists for quick searches.
Local reload capability for residents without a bank account.
Modification of resident data for seamless management.
(Refer to Figures 13, 14, 15 in the repository.)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/ef17ae4a-fc16-4a49-93e0-ac635827ccc1)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/f723170c-fd9a-421b-99cd-ff7d11e3fe0c)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/427b54c1-02da-4585-81f3-ef1ff05ff8fb)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/db55e9b2-cb2f-4450-94a3-4b63cd7a675f)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/9a4e5821-7687-4dc9-b3e6-7611cf3ba500)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/382fca22-2017-4370-b08f-8a1f1b9841ef)

# Restaurant Manager Interfaces:
Visualization of reservation metrics for efficient meal planning.
Access to already made reservations.
(Refer to Figure 16 in the repository.)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/c6c3b142-17ea-4085-814f-f2eadcfb83fe)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/e25ec774-24e3-4358-a774-fecb5ed932d1)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/18f60258-cf68-4b79-9fea-42733bef648b)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/6e40a3ab-f5f2-4c1f-8a52-8d62d2db0266)

# Admin Interfaces:
Privileged access for comprehensive system management.
User management for complete control over system functionality.
(Refer to Figures 17, 18, 19 in the repository.)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/52017261-e36f-4e77-9faa-9cb0ae7f12aa)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/4e752866-4cf1-4e9b-a0a5-a0b830c02369)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/9f055fe2-c9ae-4f25-a8a8-f034aee7ca2e)

# Verification Interfaces:
Single interface for quick verification of resident meal reservations.
Clear symbols (green, red, gray) indicating reservation status.
(Refer to Figure 20 in the repository.)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/44344fc5-29e4-40a6-9edb-c55b66c7dfb4)

![image](https://github.com/Omarouhga/gr_cu/assets/103626975/4a6f7043-59e0-43d5-a0e0-ff3ba1838b19)
![image](https://github.com/Omarouhga/gr_cu/assets/103626975/6dbf6dae-5958-4ee6-9cae-a7f07de16a9f)

# Technologies Used:
# Backend:
Odoo server with PostgreSQL for main data and MySQL for temporary reservation verification.
# Frontend:
Web-based interface accessible via standard browsers.
# Embedded Systems:
Arduino Uno, RFID cards, and Node-RED for reservation verification.

# Conclusion:
This project provides a comprehensive solution to streamline the meal reservation process and enhance verification accuracy. Server scaling considerations and potential RFID reader upgrades offer avenues for future improvements.
