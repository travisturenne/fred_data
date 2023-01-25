
import requests

import pandas as pd

from pandas.io.json import json_normalize  


 
def get_FRED_data(series_id,label):
    api_key = '488e32b30a4aa335172d3439db849fc2'
    url = 'https://api.stlouisfed.org/fred/series/observations?series_id='
    file_type = 'json'
    r_string = url+series_id+'&api_key='+api_key+'&file_type='+file_type
    data = requests.get(r_string).text
    data = pd.read_json(data, orient='records')
    data = json_normalize(data['observations'])
    data = data[['date','value']]

    data[label] = data['value']

    data = data[['date', label]]

    #Converts df to series

    #return dataframe
 
    data = data.set_index('date')
    
    data.drop(data.loc[data[label]=='.'].index, inplace=True)
    
    data = data.astype(float)


    return data

 

#metadata and brief explanation are available at https://fred.stlouisfed.org/series/series_id

#Employment Data and Production

unemployment = get_FRED_data('UNRATE', 'unemployment_rate') #Not Seasonally adjusted: UNRATENSA
net_exports = get_FRED_data('NETEXP','net_exports')

SPY = get_FRED_data('SP500','S&P500')

 

data = unemployment.merge(net_exports,how='inner', on='date')

 

data = data.set_index('date')

data=data['unemployment_rate'].astype(float)

series = pd.Series(data)

get_FRED_data('LNS14000006','black_unemplyoment_rate')

get_FRED_data('UNEMPLOY','unemployed_persons')

get_FRED_data('CIVPART', 'labour_force_participation')

get_FRED_data('LNS11300002','labour_force_participation_women')

get_FRED_data('EMRATIO','emplyoment_ratio')

get_FRED_data('ICSA','initial_unemployment_claims')

get_FRED_data('CCSA','continued_unemployment_claims')

get_FRED_data('PAYEMS','non-farm_payrolls')

get_FRED_data('LFWA64TTUSM647S', 'working_age_population')

get_FRED_data('U6RATE', 'U6_rate')

get_FRED_data('GDPC1', 'real_GDP')

get_FRED_data('CPGDPAI','GDP_change')

get_FRED_data('GNP','GNP')

get_FRED_data('INDPRO', 'industrial_production_index')

get_FRED_data('A939RX0Q048SBEA','reaL_GDP_per_capita')

get_FRED_data('MANEMP','manufacturing_employees')

get_FRED_data('OUTMS','manufacturing_real_output')



get_FRED_data('SIPOVGINIUSA','retail_and_food_sales')

get_FRED_data('RSXFS','retail_sales_excluding_food')

 

#Consumer Spending, Savings, Inflation and Interest Rates

get_FRED_data('CPIAUCSL', 'consumer_price_index_urban') #Not Seasonally adjusted: CPIAUCNS

get_FRED_data('FPCPITOTLZGUSA','consumer_price_inflation')

get_FRED_data('CPALTT01USM657N','consumer_price_growth_all_items')

get_FRED_data('PCE', 'personal_consumption_expenditures')

get_FRED_data('PCEC96','real_personal_consumption')

get_FRED_data('DSPIC96','real_disposable_income')

get_FRED_data('A229RX0','disposable_income_per_capita')

get_FRED_data('TDSP','debt_service_to_disposable_income')

get_FRED_data('UMCSENT','UofMichigan_consumer_sentiment')

get_FRED_data('PSAVERT','persoanl_savings_rate')

get_FRED_data('DGS10', 'ten_year_treasury_rate') #Daily: T10Y2Y

get_FRED_data('FEDFUNDS','federal_funds_rate')

get_FRED_data('M1', 'money_supply1')

get_FRED_data('M2', 'money_supply2')

get_FRED_data('M1V', 'money_supply1_velocity')

get_FRED_data('M2V', 'money_supply2_velocity')

get_FRED_data('BOGMBASE','monetary_base')

get_FRED_data('WALCL', 'total_assets')

get_FRED_data('T10Y3MM','10_year_expected_inflation') #daily: T10YIE

get_FRED_data('T5YIFR','5year_expected_inflation')

get_FRED_data('MICH','michigan_survey_expected_inflation')

get_FRED_data('HDTGPDUSQ163N','household_debt_to_GDP')

get_FRED_data('PI','personal_income')

 

#Public Debt and Market Data

get_FRED_data('GFDEBTN','total_public_debt')

get_FRED_data('GFDEGDQ188S', 'federal_debt_to_gdp')

get_FRED_data('AAA','AAA_corporate_bond_yield')

get_FRED_data('TB3MS','3month_tbill')

get_FRED_data('SP500','S&P500')

get_FRED_data('WILL5000INDFC','Wilshire_5000')

get_FRED_data('DDDM01USA156NWDB', 'market_captialization')

get_FRED_data('VIXCLS','CBOE_volatility_index')

get_FRED_data('TEDRATE', 'TED_spread')

get_FRED_data('USD1MTD156N', '1month_LIBOR')

get_FRED_data('DCOILWTICO','west_texas_intermediary')

get_FRED_data('MPRIME', 'bank_prime_rate')

get_FRED_data('USEPUINDXD', 'economic_policy_uncertainty_index')

get_FRED_data('BOPGSTB','trade_balance')

get_FRED_data('STLFSI2','stlouis_financial_stress_index')

get_FRED_data('W068RCQ027SBEA','government_expenditures')

#Housing

get_FRED_data('MORTGAGE15US','15year_fixed_mortgage_rate')

get_FRED_data('MSPUS','median_home_sales_price')

get_FRED_data('CSUSHPINSA', 'CASE_Shiller_Home_Price_index')

get_FRED_data('HOUST','housing_starts')

get_FRED_data('DRSFRMACBS','mortgage_delinquincies')

get_FRED_data('MSACSR','housing_supply')

get_FRED_data('PERMIT','new_building_permits')

get_FRED_data('RHORUSQ156N', 'home_ownership_rate')

get_FRED_data('HSN1F', 'single_family_home_sales')

#Other

get_FRED_data('TOTALSA','total_vehicle_sales')

get_FRED_data('ALTSALES', 'lightweight_vehicle_sales')

get_FRED_data('BUSLOANS','commercial_loans')

get_FRED_data('DPSACBW027SBOG','commercial_deposits')

get_FRED_data('DRTSCILM','domestic_banks_tigheting_percentage')

get_FRED_data('RECPROUSM156N','recession_probability')

get_FRED_data('USREC','US_recession_indicator')

get_FRED_data('CP','corporate_aftertax_profits')

get_FRED_data('DRCCLACBS', 'creditcard_delinquincies')

get_FRED_data('DGORDER','manufacturers_new_orders')

get_FRED_data('SIPOVGINIUSA','GINI_coefficient')

get_FRED_data('NCBDBIQ027S','nonfinancial_corporate_debt_securites')

get_FRED_data('ECOMPCTSA','ecommerce_sales_percentage')

get_FRED_data('POPTHM','population')

get_FRED_data('AHETPI','average_wages_nonsupervisory')

get_FRED_data('SLOAS','student_loans_securitized')

get_FRED_data('M12MTVUSM227NFWA','12month_total_vehicle_mileage')

get_FRED_data('FRGSHPUSM649NCIS','cass_freight_index')

get_FRED_data('JTSJOL','job_openings_nonfarm')

get_FRED_data('TTLCONS','total_construcion_spending')

get_FRED_data('RPONTSYD','Overnight_REPOs')

get_FRED_data('RPONTSYD','inventory_to_sales')

get_FRED_data('TOTBKCR','bank_credit')

get_FRED_data('SAVINGS','total_savings_deposits')

get_FRED_data('TOTALSL','total_securitized_credit')

 

#Producer Price Index

get_FRED_data('PPIACO','PPI_all_commodities')

get_FRED_data('PCUOMFGOMFG','PPI_all_manufacturing')

get_FRED_data('WPU101707','PPI_cold_rolled_steel')

get_FRED_data('PCUATRNWRATRNWR','PPI_transportation_and_warehousing')

get_FRED_data('PCUASHCASHC','PPI_selected_healthcare')

get_FRED_data('PCUOMINOMIN','PPI_mining')

get_FRED_data('PCUADLVWRADLVWR','PPI_delivery_and_warehousing')

get_FRED_data('PCUAMUMAMUM','total_mining_utilities_and_manufacturing')

get_FRED_data('PCUAINFOAINFO','PPI_information')

get_FRED_data('USNIM','net_interest_margin')