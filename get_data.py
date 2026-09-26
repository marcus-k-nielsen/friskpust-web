from database_connections import *




def get_latest_data(device_id):
    con, cur = database_connect()

    # Filtered by your exact database column: device_id
    cur.execute("""
        SELECT * FROM measurements 
        WHERE device_id = %s 
        ORDER BY id DESC LIMIT 1
    """, (device_id,))
    rows = cur.fetchone()

    database_close_connection(con, cur)
    return rows





def get_averages(device_id):
    con, cur = database_connect()

    # TODAY
    cur.execute("""
        SELECT 
            ROUND(AVG(temperature)::numeric, 1), 
            ROUND(AVG(humidity)::numeric, 1), 
            ROUND(AVG(co2)::numeric, 1)
        FROM measurements
        WHERE DATE(created_at) = CURRENT_DATE AND device_id = %s
    """, (device_id,))
    today = cur.fetchone()

    # WEEK - From Monday to Saturday
    cur.execute("""
        SELECT 
            ROUND(AVG(temperature)::numeric, 1), 
            ROUND(AVG(humidity)::numeric, 1), 
            ROUND(AVG(co2)::numeric, 1)
        FROM measurements
        WHERE created_at >= DATE_TRUNC('week', NOW()) AND device_id = %s
    """, (device_id,))
    week = cur.fetchone()

    # MONTH - From the 1st of the calendar month
    cur.execute("""
        SELECT 
            ROUND(AVG(temperature)::numeric, 1), 
            ROUND(AVG(humidity)::numeric, 1), 
            ROUND(AVG(co2)::numeric, 1)
        FROM measurements
        WHERE created_at >= DATE_TRUNC('month', NOW()) AND device_id = %s
    """, (device_id,))
    month = cur.fetchone()

    database_close_connection(con, cur)

    return {
        "today": {"temp": today[0] if today[0] is not None else 0, "humidity": today[1] if today[1] is not None else 0, "air": today[2] if today[2] is not None else 0},
        "week": {"temp": week[0] if week[0] is not None else 0, "humidity": week[1] if week[1] is not None else 0, "air": week[2] if week[2] is not None else 0},
        "month": {"temp": month[0] if month[0] is not None else 0, "humidity": month[1] if month[1] is not None else 0, "air": month[2] if month[2] is not None else 0}
    }