# Version 3.0
import tkinter
import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime as dt
from tkinter import messagebox


# Layout

root = tk.Tk()
root.geometry('650x250')
root.title('Santos Json Tool 3.0')
#root.resizable(0, 0)

# Labels of widget
ttk.Label(root, text='Tracking Json Generator', foreground='Black', font=('aria', 15, 'bold')).grid(column=0, row=1,
                                                                                                    sticky=tk.NE)
ttk.Label(root, text="Tracking ID :", font=("Times New Roman", 13)).grid(column=0, row=5, sticky=tk.W, padx=20, pady=10)
ttk.Label(root, text="Carrier Code :", font=("Times New Roman", 13)).grid(column=0, row=6, sticky=tk.W, padx=20,
                                                                          pady=10)
ttk.Label(root, text="Event Type :", font=("Times New Roman", 13)).grid(column=0, row=7, sticky=tk.W, padx=20, pady=10)
ttk.Label(root, text="Events :", font=("Times New Roman", 13)).grid(column=0, row=8, sticky=tk.W, padx=20, pady=10)
ttk.Label(root, text="Gendrated at :", font=("Times New Roman", 13)).grid(column=0, row=9, sticky=tk.W, padx=20, pady=10)
# Input Tracking ID
trackingid_var = tk.StringVar()
trackingid_entry = ttk.Entry(root, width=48, textvariable=trackingid_var)
trackingid_entry.grid(column=1, row=5)

# Combobox Carrier Code
carriercode_var = tk.StringVar()
carriercode_entry = ttk.Combobox(root, width=45, textvariable=carriercode_var)
carriercode_entry['values'] = ('fedex', 'usps', 'ups', 'amazon', 'amzl')
carriercode_entry.current(0)
carriercode_entry.grid(column=1, row=6)
carriercode_entry.current()

# Combobox type of event
eventtype_var = tk.StringVar()
eventtype_entry = ttk.Combobox(root, width=45, textvariable=eventtype_var)
eventtype_entry['values'] = ('Live', '14 days before', '45 days before')
eventtype_entry.current(0)
eventtype_entry.grid(column=1, row=7)
eventtype_entry.current()

# Combobox Events
events_var = tk.StringVar()
events_entry = ttk.Combobox(root, width=45)
events_entry['values'] = ("[Shipped] - IN_TRANSIT_001",
                          "[On. way] - ON_THE_WAY_001",
                          "[On Hold] - ON_HOLD_001",
                          "[Delayed] - DELAYED_001",
                          "[D.Fu.W.EDD] - DELAYED_001",
                          "[D.Fu.WO.EDD] - DELAYED_001",
                          "[D.Pa.W.EDD] - DELAYED_001",
                          "[D.Pa.WO.EDD] - DELAYED_001",
                          "[D.Fu.W.EDD] - DELAYED_003",
                          "[D.Fu.WO.EDD] - DELAYED_003",
                          "[D.Pa.W.EDD] - DELAYED_003",
                          "[D.Pa.WO.EDD] - DELAYED_003",
                          "[H at C] - DELAYED_002",
                          "[A'P] - AVAILABLE_FOR_PICKUP_001",
                          "[O'D] - OUT_FOR_DELIVERY_001",
                          "[DA] - DELIVERY_ATTEMPTED_001",
                          "[H'P at CL] - AVAILABLE_FOR_PICKUP_001",
                          "[] - EXCEPTION_001",
                          "[Customer moved] - EXCEPTION_002",
                          "[Incorrect Address] - EXCEPTION_007",
                          "[Cancelled] - EXCEPTION_008",
                          "[Rejected by carrier] - EXCEPTION_009",
                          "[Undeliverable] - UNDELIVERABLE_001",
                          "[Sp. Damaged] - UNDELIVERABLE_002",
                          "[] - RETURN_TO_SENDER_001",
                          "[Cus. Refused] - RETURN_TO_SENDER_002",
                          "[] - RETURN_TO_SENDER_003",
                          "[] - RETURN_TO_SENDER_004",
                          "[Lost] - UNDELIVERABLE_003",
                          "[Delivered] - DELIVERED_001",
                          "[Expired] - EXPIRED_001")

events_entry.current(0)
events_entry.grid(column=1, row=8)
events_entry.current()


def click():
    # Converting Human readable Date & Time to Timestamp
    normaltime = int(dt.timestamp(dt.now()))
    epoachlivetime = normaltime * 1000
    timechange = epoachlivetime

    # Type of event Time Choosing
    if eventtype_entry.get() == "live":
        timechange = epoachlivetime
    elif eventtype_entry.get() == "14 days before":
        timechange = (epoachlivetime - 1209600000)
    elif eventtype_entry.get() == "45 days before":
        timechange = (epoachlivetime - 3888000000)

    info_received_001 = {"trackingId": trackingid_entry.get(),  # Filling the Dict by auto input from the text entry field
               "carrierCode": carriercode_entry.get(),
               "code": "INFO_RECEIVED",
               "subCode": "INFO_RECEIVED_001",
               "estimatedDeliveryTimestamp": timechange + 18000000,
               "updatedTimestamp": timechange,
               "eventsList": [
                   {
                       "location": {
                           "city": "hyd",
                           "country": "IND",
                           "landmark": "random",
                           "state": "ts",
                           "zipCode": "500001"
                       },
                       "status": {
                           "code": "INFO_RECEIVED",
                           "subCode": "INFO_RECEIVED_001",
                           "details": "Order Placed",
                           "statusTimestamp": timechange
                       }
                   }
               ]
               }

    in_transit_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "IN_TRANSIT",
        "subCode": "IN_TRANSIT_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    on_hold_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "CUSTOMER_ACTION",
        "subCode": "CUSTOMER_ACTION_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 120000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "CUSTOMER_ACTION",
                    "subCode": "CUSTOMER_ACTION_001",
                    "details": "Package on hold",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_01 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_001",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_future_with_EDD_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_001",
        "estimatedDeliveryTimestamp": timechange + 36000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_001",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_future_without_EDD_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_001",
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_001",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_past_with_EDD_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_001",
        "estimatedDeliveryTimestamp": timechange - 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_001",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_past_without_EDD_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_001",
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_001",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_future_with_EDD_003 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_003",
        "estimatedDeliveryTimestamp": timechange + 36000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_003",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_future_without_EDD_003 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_003",
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_003",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_past_with_EDD_003 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_003",
        "estimatedDeliveryTimestamp": timechange - 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_003",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_past_without_EDD_003 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_003",
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_003",
                    "details": "Package delay",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delayed_002 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELAYED",
        "subCode": "DELAYED_002",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELAYED",
                    "subCode": "DELAYED_002",
                    "details": "Package is Held at customs",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    available_for_pickup_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "AVAILABLE_FOR_PICKUP",
        "subCode": "AVAILABLE_FOR_PICKUP_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package is Shipped",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Available for Pickup",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    out_for_delivery_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "OUT_FOR_DELIVERY",
        "subCode": "OUT_FOR_DELIVERY_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delivery_attempted_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELIVERY_ATTEMPTED",
        "subCode": "DELIVERY_ATTEMPTED_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    held_pickup_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "AVAILABLE_FOR_PICKUP",
        "subCode": "AVAILABLE_FOR_PICKUP_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempted",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Package is held for Pickup at carrier location",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    execp_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "EXCEPTION",
        "subCode": "EXCEPTION_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 3000000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempted",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Package is Available for Pickup",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "EXCEPTION",
                    "subCode": "EXCEPTION_001",
                    "details": "Order Cancelled",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    execp_002 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "EXCEPTION",
        "subCode": "EXCEPTION_002",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 3000000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempted",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Package is Available for Pickup",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "EXCEPTION",
                    "subCode": "EXCEPTION_002",
                    "details": "Order Cancelled",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    execp_007 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "EXCEPTION",
        "subCode": "EXCEPTION_007",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 3000000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempted",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Package is Available for Pickup",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "EXCEPTION",
                    "subCode": "EXCEPTION_007",
                    "details": "Order Cancelled",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    execp_008 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "EXCEPTION",
        "subCode": "EXCEPTION_008",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 3000000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempted",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Package is Available for Pickup",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "EXCEPTION",
                    "subCode": "EXCEPTION_008",
                    "details": "Order Cancelled",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    excep_009 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "EXCEPTION",
        "subCode": "EXCEPTION_009",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 3000000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempted",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "AVAILABLE_FOR_PICKUP",
                    "subCode": "AVAILABLE_FOR_PICKUP_001",
                    "details": "Package is Available for Pickup",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "EXCEPTION",
                    "subCode": "EXCEPTION_009",
                    "details": "Order Cancelled",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    undeliverable_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "UNDELIVERABLE",
        "subCode": "UNDELIVERABLE_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "UNDELIVERABLE",
                    "subCode": "UNDELIVERABLE_001",
                    "details": "Package is Undeliverable",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    undeliverable_002 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "UNDELIVERABLE",
        "subCode": "UNDELIVERABLE_002",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "UNDELIVERABLE",
                    "subCode": "UNDELIVERABLE_002",
                    "details": "Package is Undeliverable",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    sender_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "RETURN_TO_SENDER",
        "subCode": "RETURN_TO_SENDER_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "RETURN_TO_SENDER",
                    "subCode": "RETURN_TO_SENDER_001",
                    "details": "Package is Undeliverable",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    sender_002 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "RETURN_TO_SENDER",
        "subCode": "RETURN_TO_SENDER_002",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "RETURN_TO_SENDER",
                    "subCode": "RETURN_TO_SENDER_002",
                    "details": "Package is Undeliverable",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    sender_003 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "RETURN_TO_SENDER",
        "subCode": "RETURN_TO_SENDER_003",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "RETURN_TO_SENDER",
                    "subCode": "RETURN_TO_SENDER_003",
                    "details": "Package is Undeliverable",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    sender_004 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "RETURN_TO_SENDER",
        "subCode": "RETURN_TO_SENDER_004",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package Shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "RETURN_TO_SENDER",
                    "subCode": "RETURN_TO_SENDER_004",
                    "details": "Package is Undeliverable",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    undeliverable_003 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "UNDELIVERABLE",
        "subCode": "UNDELIVERABLE_003",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERY_ATTEMPTED",
                    "subCode": "DELIVERY_ATTEMPTED_001",
                    "details": "Delivery Attempt",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "UNDELIVERABLE",
                    "subCode": "UNDELIVERABLE_003",
                    "details": "Package is lost",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    delivered_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "DELIVERED",
        "subCode": "DELIVERED_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package shipped",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERED",
                    "subCode": "DELIVERED_001",
                    "details": "Package Delivered",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    expired_001 = {
        "trackingId": trackingid_entry.get(),
        "carrierCode": carriercode_entry.get(),
        "code": "EXPIRED",
        "subCode": "EXPIRED_001",
        "estimatedDeliveryTimestamp": timechange + 18000000,
        "updatedTimestamp": timechange,
        "eventsList": [
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "INFO_RECEIVED",
                    "subCode": "INFO_RECEIVED_001",
                    "details": "Order Placed",
                    "statusTimestamp": timechange - 2400000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "IN_TRANSIT",
                    "subCode": "IN_TRANSIT_001",
                    "details": "Package shipped",
                    "statusTimestamp": timechange - 1800000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "OUT_FOR_DELIVERY",
                    "subCode": "OUT_FOR_DELIVERY_001",
                    "details": "Package is Out for Delivery",
                    "statusTimestamp": timechange - 1200000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "DELIVERED",
                    "subCode": "DELIVERED_001",
                    "details": "Package Delivered",
                    "statusTimestamp": timechange - 600000
                }
            },
            {
                "location": {
                    "city": "hyd",
                    "country": "IND",
                    "landmark": "random",
                    "state": "ts",
                    "zipCode": "500001"
                },
                "status": {
                    "code": "EXPIRED",
                    "subCode": "EXPIRED_001",
                    "details": "Tracking expired",
                    "statusTimestamp": timechange
                }
            }
        ]
    }

    # noinspection PyGlobalUndefined
    def eve():
        global trigger
        if events_entry.get() == '[Shipped] - IN_TRANSIT_001':  # Combobox input in Events to pick the JSON
            trigger = info_received_001
        elif events_entry.get() == '[On. way] - ON_THE_WAY_001':
            trigger = in_transit_001
        elif events_entry.get() == '[On Hold] - ON_HOLD_001':
            trigger = on_hold_001
        elif events_entry.get() == '[Delayed] - DELAYED_001':
            trigger = delayed_01
        elif events_entry.get() == '[D.Fu.W.EDD] - DELAYED_001':
            trigger = delayed_future_with_EDD_001
        elif events_entry.get() == '[D.Fu.WO.EDD] - DELAYED_001':
            trigger = delayed_future_without_EDD_001
        elif events_entry.get() == '[D.Pa.W.EDD] - DELAYED_001':
            trigger = delayed_past_with_EDD_001
        elif events_entry.get() == '[D.Pa.WO.EDD] - DELAYED_001':
            trigger = delayed_past_without_EDD_001
        elif events_entry.get() == '[D.Fu.W.EDD] - DELAYED_003':
            trigger = delayed_future_with_EDD_003
        elif events_entry.get() == '[D.Fu.WO.EDD] - DELAYED_003':
            trigger = delayed_future_without_EDD_003
        elif events_entry.get() == '[D.Pa.W.EDD] - DELAYED_003':
            trigger = delayed_past_with_EDD_003
        elif events_entry.get() == '[D.Pa.WO.EDD] - DELAYED_003':
            trigger = delayed_past_without_EDD_003
        elif events_entry.get() == '[H at C] - DELAYED_002':
            trigger = delayed_002
        elif events_entry.get() == "[A'P] - AVAILABLE_FOR_PICKUP_001":
            trigger = available_for_pickup_001
        elif events_entry.get() == "[O'D] - OUT_FOR_DELIVERY_001":
            trigger = out_for_delivery_001
        elif events_entry.get() == '[DA] - DELIVERY_ATTEMPTED_001':
            trigger = delivery_attempted_001
        elif events_entry.get() == "[H'P at CL] - AVAILABLE_FOR_PICKUP_001":
            trigger = held_pickup_001
        elif events_entry.get() == '[] - EXCEPTION_001':
            trigger = execp_001
        elif events_entry.get() == '[Customer moved] - EXCEPTION_002':
            trigger = execp_002
        elif events_entry.get() == '[Incorrect Address] - EXCEPTION_007':
            trigger = execp_007
        elif events_entry.get() == '[Cancelled] - EXCEPTION_008':
            trigger = execp_008
        elif events_entry.get() == '[Rejected by carrier] - EXCEPTION_009':
            trigger = excep_009
        elif events_entry.get() == '[Undeliverable] - UNDELIVERABLE_001':
            trigger = undeliverable_001
        elif events_entry.get() == '[Sp. Damaged] - UNDELIVERABLE_002':
            trigger = undeliverable_002
        elif events_entry.get() == '[] - RETURN_TO_SENDER_001':
            trigger = sender_001
        elif events_entry.get() == '[Cus. Refused] - RETURN_TO_SENDER_002':
            trigger = sender_002
        elif events_entry.get() == '[] - RETURN_TO_SENDER_003':
            trigger = sender_003
        elif events_entry.get() == '[] - RETURN_TO_SENDER_004':
            trigger = sender_004
        elif events_entry.get() == '[Lost] - UNDELIVERABLE_003':
            trigger = undeliverable_003
        elif events_entry.get() == '[Delivered] - DELIVERED_001':
            trigger = delivered_001
        elif events_entry.get() == '[Expired] - EXPIRED_001':
            trigger = expired_001
        if trackingid_entry.get() == "":
            messagebox.showerror("Tracking ID Error", "Error: Please Enter the Tracking ID")
        else:
            top = tk.Toplevel(root)
            top.geometry("700x500")
            entry = tkinter.Text(top, height=30, bd=3, padx=30, pady=10)
            entry.pack()

            entry.insert(tk.INSERT, json.dumps(trigger, indent=4))

        now = dt.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        text = tk.Text(root, height=1, width=20)
        text.place(x=200, y=210)
        text.insert(tk.INSERT, dt_string)
    eve()


def generate():

    click()


btn = ttk.Button(root, text="Generate", command=generate)
btn.place(x=500, y=210)

root.mainloop()
