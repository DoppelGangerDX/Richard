
from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient

client = PIWebApiClient("https://test.osisoft.com/piwebapi", False, "username", "password", True)

#df1 = client.data.get_recorded_values("pi:\\\\JUPITER001\\cdt158", None, None, "*-9d", None, None, None, None, "*-10d", None)
df1 =  client.element.get_by_path("\\\\JUPITER001\\Universities\\UC Davis", None)
# df4 = client.data.get_multiple_recorded_values(["pi:\\JUPITER001\sinusoid", "pi:\\JUPITER001\sinusoidu", "pi:\\JUPITER001\cdt158"], None, "*", None, None, None,  None, "*-1d", None)
# df2 = client.data.get_interpolated_values("pi:\\JUPITER001\\sinusoidu", None, "*", None, None, "2h", None, "*-1d", None)
# df3 = client.data.get_plot_values("pi:\\\\JUPITER001\\sinusoidu", None, "*", 10, None, "*-3d", None)
# df4 = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", None, None, "*", None, None, None, "items.value;items.timestamp", "*-1d", None)
# df5 = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", None, None, "*", None, None, None, "items.good;items.questionable;items.substituted", "*-1d", None)

print(df1)