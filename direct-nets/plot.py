import matplotlib.pyplot as plt
items = [
76200.2,
56540.1,
33760.0,
31656.7,
26798.6,
27129.3,
26657.1,
23994.1,
23944.1,
24590.1,
21342.8,
18300.4,
20784.1,
19400.1,
17715.1,
16601.7,
16879.9,
15579.8,
15527.2,
14819.6,
15132.2,
13938.5,
13456.7,
12234.2,
12861.0,
12012.1,
10422.1,
10087.0,
9602.18,
9498.89,
8832.74,
8497.27,
9164.53,
9385.68,
7591.29,
8014.08,
7999.14,
7947.46,
7705.69,
7631.61,
6980.18,
6949.05,
6957.27,
6972.08,
6879.72,
6692.95,
5911.51,
6521.67,
6611.33,
5854.86,
6217.16,
6501.47,
6132.03,
6237.64,
6179.34,
5678.43,
5640.06,
6278.11,
5624.88,
6199.1,
5858.32,
6063.7,
5701.09,
5819.65,
5940.63,
5502.03,
6112.43,
5652.31,
5920.05,
5737.68,
5428.29,
5419.54,
5732.37,
5539.59,
5752.49,
6027.46,
5679.2,
5607.22,
5645.97,
5228.06,
5564.43,
5764.97,
5970.54,
5243.4,
6495.72,
5926.08,
5786.55,
5280.37,
5326.34,
5421.77,
5439.77,
5563.72,
5575.31,
5123.34,
5330.79,
5542.11,
5457.7,
5376.93,
5555.59,
3987.17,
3353.46,
6465.85,
2821.4,
3246.42,
2368.66,
2579.75,
2105.75,
2498.43,
2204.66,
2465.29,
2561.77,
2412.47,
2219.04,
4863.34,
2023.97,
1922.73,
1895.06,
2192.44,
2370.64,
2061.57,
1850.99,
1995.67,
1867.88,
1954.29,
1702.28,
1814.81,
1654.39,
1605.08,
1646.21,
1872.81,
2189.28,
2057.72,
1716.37,
1790.57,
1613.21,
1720.62,
1702.05,
31511.3,
8959.42,
6588.47,
4439.39,
3977.28,
3823.28,
2942.87,
2638.22,
2119.09,
2687.44,
2298.92,
1900.07,
1786.39,
1892.78,
24779.7,
5007.45,
3045.04,
2353.44,
1859.51,
1763.49,
1741.28,
1623.14,
1613.67,
1653.93,
1387.51,
2034.63,
1828.97,
1672.63,
1658.34,
1564.3,
1563.64,
1563.18,
1416.05,
1460.97,
1626.07,
2912.53,
1570.03,
1536.12,
1312.71,
1731.22,
1458.17,
1764.46,
1586.93,
1497.34,
1476.26,
1503.24,
1550.16,
1648.36,
1550.77,
1464.33,
1447.06,
1658.35,
1403.73,
1324.29,
2010.96,
1524.29,
1461.66,
1631.84,
1399.87,
1439.78,
1729.65,
1578.92,
1574.2,
1647.99,
1460.08,
7275.77,
1795.17,
1372.53,
1365.14,
1515.55,
1405.01,
1469.93,
1294.83,
1374.66,
1216.26,
1205.59,
1648.87,
1510.46,
1264.49,
1604.64,
1505.39,
1454.84,
1328.19,
1345.03,
1229.12,
1241.4,
1279.99,
1454.95,
1624.7,
1375.78,
1230.57,
1453.21,
1619.78,
26054.0,
13816.3,
4904.04,
3837.57,
3324.5,
3006.93,
2687.34,
1586.5,
1499.07,
1429.51,
1549.71,
1620.67,
1312.1,
1215.39,
1396.88,
17557.5,
1294.79,
1475.69,
1323.06,
1472.64,
1206.65,
1316.25,
1371.73,
1296.05,
1222.56,
1270.0,
1210.82,
1244.92,
1226.27,
1325.46,
1126.49,
1454.38,
1232.16,
1598.9,
1675.66,
1244.69,
1502.42,
1315.7,
1397.75,
1397.34,
1239.63,
8399.81,
1777.6,
1305.2,
1413.12,
1462.41,
1142.74,
1428.37,
1251.12,
1251.94,
1555.04,
1473.15,
1371.71,
1175.62,
1302.65,
1164.71,
1158.06,
1207.56,
1212.68,
1560.94,
1134.35,
1246.0,
1431.88,
1519.81,
1304.79,
1201.85,
1183.8,
1247.26,
1125.17,
1193.17,
1317.86,
1287.57,
1288.83,
25854.2,
1232.29,
1249.17,
1147.73,
1424.17,
3169.21,
1300.94,
1198.87,
1327.69,
1323.68,
1136.15,
1395.74,
1386.24,
1245.63,
1540.56,
1164.73,
1565.56,
1264.86,
1214.74,
1228.28,
1192.72,
1221.1,
1256.05,
1134.09,
11703.3,
1138.35,
1088.18,
1051.9,
1374.65,
1187.35,
1122.59,
1091.74,
1160.28,
1088.56,
1097.61,
1277.02,
1173.53,
1575.88,
1240.04,
1298.48,
1271.57,
1061.56,
927.162,
1133.48,
1168.15,
1117.99,
1107.86,
1127.58,
949.306,
946.164,
1214.89,
960.668,
1226.71,
1399.48,
1022.82,
1192.81,
1252.47,
1052.87,
1742.96,
1297.19,
1407.33,
1040.54,
1136.12,
1474.23,
1495.03,
1266.05,
1264.42,
1077.13,
921.675,
904.361,
1243.29,
1015.93,
1055.68,
917.809,
1448.74,
1197.48,
1178.98,
1212.75,
1149.34,
975.878,
1239.16,
963.595,
6883.78,
1476.14,
1131.92,
1108.58,
1231.38,
22356.4,
1451.64,
1053.38,
1193.06,
1131.58,
979.647,
1291.08,
1113.44,
1012.89,
1051.32,
1143.16,
916.098,
1070.96,
1027.31,
1089.24,
954.345,
1158.87,
1159.88,
1036.98,
1146.6,
1260.56,
926.529,
1009.98,
1154.27,
1049.62,
847.409,
946.897,
1512.69,
1113.17,
1058.49,
1115.38,
931.786,
948.445,
1277.24,
1114.28,
1046.03,
1041.93,
1124.17,
926.701,
997.945,
1112.81,
1138.37,
915.07,
949.651,
1176.2,
1387.88,
1238.09,
1188.42,
1009.12,
1059.21,
1070.0,
1047.4,
1119.28,
1048.98,
932.203,
939.977,
1043.88,
1030.7,
10393.6,
913.408,
1154.29,
1080.62,
1126.19,
1038.1,
1010.23,
958.543,
1122.38,
977.533,
1088.1,
1105.47,
932.234,
1147.21,
1016.54,
970.678,
1023.28,
1071.06,
1019.46,
1101.13,
949.649,
1223.55,
1028.46,
1478.36,
1159.41,
1110.27,
1121.74,
910.82,
1095.64,
1037.09,
1278.0,
973.978,
1153.15,
992.014,
1151.14,
1106.18,
1048.77,
789.422,
911.987,
973.679,
898.096,
1037.08,
928.55,
1110.49,
915.634,
983.826,
1042.75,
1214.14,
2324.02,
1352.6,
1200.87,
973.817,
1161.3,
976.339,
935.434,
1067.11,
1112.78,
911.669,
1171.58,
1137.66,
4556.59,
1189.55,
1376.52,
931.411,
1010.33,
1180.35,
1308.41,
1253.78,
959.179,
899.835,
1165.89,
980.794,
2588.53,
1106.78,
1035.64,
948.751,
1380.43,
1118.75,
1328.88,
1153.37,
1118.1,
900.847,
1062.32,
1147.12,
950.505,
888.407,
1063.41,
1027.96,
828.521,
1202.2,
1161.15,
979.096,
1077.04,
1090.81,
1049.06,
850.953,
1054.91,
998.394,
1116.99,
1114.88,
897.055,
1250.97,
1194.51,
1011.67,
1116.76,
1059.25,
947.168,
1019.86,
878.918,
1159.74,
1132.75,
1125.75,
991.517,
939.343,
1112.28,
1075.23,
1002.7,
950.057,
1033.75,
1100.89,
949.155,
777.048,
930.912,
903.923,
993.807,
941.379,
944.701,
955.077,
914.174,
866.732,
1224.39,
18372.1,
1205.42,
1077.31,
914.151,
947.076,
941.434,
945.412,
804.497,
1158.1,
964.011,
823.784,
1021.18,
1010.51,
965.506,
929.228,
936.24,
916.645,
983.26,
1138.73,
961.179,
866.7,
1085.55,
871.288,
990.046,
916.979,
888.996,
888.698,
1057.79,
805.378,
1118.39,
886.016,
1139.57,
829.237,
888.022,
963.388,
812.593,
990.628,
836.148,
1014.2,
883.613,
1002.41,
895.491,
903.286,
1078.47,
1189.14,
1112.44,
875.488,
784.142,
932.474,
1062.3,
1021.91,
840.02,
950.588,
17089.1,
955.179,
961.283,
1002.84,
800.463,
944.291,
1100.64,
1026.01,
1486.49,
1214.78,
867.591,
897.651,
887.519,
1063.32,
991.707,
1146.56,
1050.71,
952.308,
892.996,
854.549,
999.477,
958.341,
786.936,
2654.56,
1073.11,
854.459,
875.239,
792.187,
945.939,
913.518,
1154.24,
910.623,
761.894,
1104.62,
797.427,
985.934,
828.249,
754.781,
918.643,
1053.27,
1021.72,
1033.86,
882.615,
940.706,
885.222,
1370.79,
966.799,
982.353,
924.3,
936.79,
868.292,
929.927,
1033.85,
806.536,
795.024,
1558.33,
1070.55,
901.808,
952.345,
909.041,
975.493,
919.447,
897.629,
887.571,
995.197,
937.604,
1012.14,
925.886,
1315.91,
1412.42,
939.892,
815.274,
852.298,
1034.2,
856.352,
973.402,
768.414,
876.427,
924.404,
1039.42,
892.619,
963.379,
1018.75,
1973.85,
1029.9,
983.716,
934.086,
984.108,
1066.08,
1344.71,
813.839,
1001.83,
834.965,
838.2,
852.273,
889.334,
844.488,
886.996,
801.627,
946.327,
925.382,
910.486,
835.825,
846.252,
841.569,
892.508,
963.587,
798.437,
4348.63,
925.548,
908.819,
911.772,
974.015,
948.231,
933.058,
869.725,
970.851,
885.056,
929.195,
900.617,
878.614,
833.044,
836.504,
864.906,
806.539,
907.549,
933.7,
903.422,
798.963,
1008.16,
1040.96,
937.673,
940.086,
850.456,
981.923,
800.547,
920.479,
868.006,
867.966,
971.686,
888.95,
757.239,
1033.38,
809.949,
896.133,
933.34,
885.631,
1623.06,
1052.55,
788.366,
990.853,
873.02,
745.212,
1002.88,
873.767,
1776.07,
1047.41,
1051.67,
935.602,
863.602,
927.969,
915.394,
700.108,
801.22,
983.386,
820.958,
1009.69,
879.803,
755.045,
1007.4,
801.507,
1025.33,
827.784,
1158.26,
796.767,
978.564,
1041.24,
845.706,
835.175,
872.755,
953.141,
782.722,
985.13,
752.49,
912.931,
1036.63,
1011.89,
826.688,
963.248,
977.118,
840.775,
853.681,
933.032,
1030.72,
684.102,
1433.33,
820.893,
802.087,
868.405,
793.938,
953.248,
931.137,
922.155,
802.93,
917.532,
885.822,
824.42,
830.826,
1014.46,
769.242,
934.512,
732.417,
812.815,
747.232,
906.139,
912.987,
887.627,
1206.18,
1040.21,
875.165,
724.31,
932.447,
877.285,
675.755,
867.487,
955.91,
919.166,
805.693,
917.026,
762.622,
1027.56,
800.317,
839.253,
1483.66,
1108.89,
1060.2,
1089.48,
918.398,
781.945,
748.184,
905.819,
917.618,
767.906,
918.916,
3976.34,
1050.74,
803.056,
851.75,
954.242,
785.08,
855.291,
886.471,
901.974,
749.451,
694.71,
804.843,
966.987,
934.271,
899.537,
776.83,
787.158,
880.94,
1002.98,
854.061,
815.091,
954.582,
790.232,
810.179,
853.172,
916.902,
877.861,
822.47,
1181.08,
947.289,
959.319,
1034.12,
1024.71,
1057.19,
854.596,
989.26,
956.456,
902.785,
788.0,
703.947,
1127.32,
804.222,
858.193,
928.935,
815.116,
826.567,
739.143,
764.696,
1166.37,
875.272,
820.215,
938.508,
614.838,
862.808,
1013.5,
1046.67,
988.358,
835.712,
782.375,
782.81,
817.906,
820.222,
836.683,
758.298,
977.093,
956.763,
756.649,
952.813,
978.041,
698.562,
956.828,
906.746,
926.8,
857.684,
845.023,
761.468,
738.78,
757.052,
886.285,
1004.99,
919.729,
879.938,
799.242,
846.299,
975.132,
847.475,
831.07,
797.059,
805.428,
14821.3,
1052.62,
924.197,
1007.44,
801.88,
806.496,
859.988,
839.518,
793.025,
825.5,
866.486,
785.949,
814.477,
851.069,
958.77,
1034.66,
844.205,
713.198,
777.569,
1039.04,
839.09,
865.16,
765.523,
788.638,
707.022,
750.427,
1095.98,
951.998,
862.883,
819.586,
817.261,
726.117,
814.111,
837.61,
908.085,
724.936,
785.793,
798.914,
807.952,
914.311,
935.978,
750.745,
816.459,
1018.1,
800.905,
869.274,
749.823,
886.375,
750.911,
836.996,
708.018,
897.307,
874.518,
891.426,
838.792,
811.251,
948.597,
911.667,
668.702,
822.342,
1298.11,
1114.06,
829.388,
932.622,
757.267,
982.157,
851.156,
824.671,
820.872,
930.618,
864.469,
777.596,
927.113,
814.079,
808.182,
914.615,
936.139,
988.422,
906.403,
704.866,
941.389,
855.376,
826.079,
879.806,
890.505,
808.896,
976.225,
850.321,
859.233,
915.083,
833.494,
866.204,
971.672,
1001.6,
790.759,
1180.33,
886.444,
828.706,
823.511,
858.597,
737.565,
878.141,
864.262,
778.106,
890.467,
816.724,
725.302,
854.489,
819.706,
700.649,
757.861,
1112.02,
851.356,
1108.73,
817.548,
867.956,
922.805,
732.976,
897.495,
699.119,
978.461,
874.422,
1001.19,
907.285,
989.395,
919.782,
778.2,
769.749,
729.73,
747.901,
786.271,
813.066,
911.793,
791.793,
830.777,
831.878,
874.442,
767.719,
784.326,
630.007,
646.67,
747.09,
699.147,
902.303,
1025.98,
735.402,
675.73,
963.757,
966.558,
848.413,
912.277,
804.161,
792.553,
711.171,
704.938,
765.729,
866.885,
876.626,
688.085,
780.536,
719.866,
851.757,
758.419,
812.328,
773.93,
929.672,
788.363,
802.16,
821.764,
899.106,
745.274,
856.967,
861.704,
760.546,
869.966,
799.628,
738.077,
805.764,
1139.46,
901.618,
1018.43,
1021.32,
794.561,
864.231,
1083.71,
883.132,
2168.81,
877.652,
928.755,
669.701,
798.282,
807.418,
766.358,
847.632,
780.847,
851.262,
838.88,
742.621,
747.762,
765.305,
953.195,
789.506,
834.392,
696.338,
801.815,
808.5,
803.025,
814.035,
875.828,
769.647,
773.975,
747.3,
836.749,
849.857,
870.631,
726.367,
784.806,
717.364,
681.797,
640.645,
759.052,
763.393,
838.214,
817.894,
864.702,
723.149,
712.022,
888.142,
833.081,
1022.6,
885.262,
739.803,
882.162,
945.704,
730.54,
846.361,
744.568,
776.44,
752.669,
838.793,
818.926,
889.086,
755.273,
898.896,
694.085,
838.96,
908.667,
844.251,
684.81,
782.006,
2362.91,
1066.87,
892.822,
784.346,
755.255,
906.095,
854.135,
774.739,
741.405,
681.006,
892.233,
864.681,
775.094,
735.383,
1068.65,
820.436,
698.225,
706.489,
710.321,
709.614,
818.753,
919.367,
860.886,
705.478,
819.636,
815.286,
749.786,
826.038,
812.441,
699.012,
975.852,
826.915,
1214.66,
800.535,
717.717,
1012.84,
804.647,
917.935,
737.493,
721.957,
698.867,
894.395,
825.247,
803.763,
706.119,
838.591,
680.34,
697.881,
642.751,
904.214,
11787.9,
898.016,
885.913,
917.793,
1009.54,
907.135,
1008.08,
862.377,
743.123,
799.289,
748.232,
1074.04,
678.326,
2003.89,
673.454,
744.74,
778.522,
863.967,
862.527,
852.197,
836.841,
791.008,
714.15,
817.607,
710.404,
803.997,
825.731,
772.555,
1037.19,
775.053,
753.121,
855.781,
1175.69,
720.929,
811.824,
810.145,
733.741,
785.306,
750.055,
797.378,
899.101,
3468.41,
872.647,
814.582,
902.811,
789.824,
815.311,
853.275,
713.878,
1239.56,
759.335,
888.626,
792.208,
1038.61,
729.033,
807.541,
788.448,
810.251,
848.586,
765.833,
750.536,
982.791,
685.883,
734.205,
755.161,
872.162,
886.31,
840.429,
916.772,
764.955,
898.582,
629.972,
791.311,
755.319,
903.479,
725.823,
748.721,
822.858,
808.983,
759.511,
896.242,
693.72,
756.579,
679.791,
895.902,
870.398,
663.683,
770.741,
848.829,
828.859,
]
y = [x+30 for x in range(len(items))]
plt.plot(y, items)
plt.show()