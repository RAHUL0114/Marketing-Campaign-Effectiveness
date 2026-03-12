
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('cleaned_marketing_campaign.csv')
except FileNotFoundError:
    st.error("Dataset file 'cleaned_marketing_campaign.csv' not found. Please ensure it's in the same directory.")
    st.stop() # Stop the app if the dataset is not found

st.title("Marketing Campaign Dashboard")

# 1. Histogram: Distribution of Conversion Rates
st.subheader("Distribution of Conversion Rates")
fig, ax = plt.subplots()
sns.histplot(df['Conversion_Rate'], kde=True, ax=ax)
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This histogram shows the distribution of conversion rates across all campaigns.
*   Most campaigns have a conversion rate between 0.05 and 0.1.
*   Understanding this distribution helps set realistic conversion goals and identify outlier campaigns.
""")

# 2. Bar Chart: Average Conversion Rate by Campaign Type
st.subheader("Average Conversion Rate by Campaign Type")
fig, ax = plt.subplots()
sns.barplot(x='Campaign_Type', y='Conversion_Rate', data=df.groupby('Campaign_Type')['Conversion_Rate'].mean().reset_index(), ax=ax)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This chart compares the average conversion rates of different campaign types.
*   Identify which campaign types are most effective at driving conversions.
*   Allocate resources to high-performing campaign types or investigate ways to improve lower-performing ones.
""")

# 3. Bar Chart: Average ROI by Channel Used
st.subheader("Average ROI by Channel Used")
fig, ax = plt.subplots()
sns.barplot(x='Channel_Used', y='ROI', data=df.groupby('Channel_Used')['ROI'].mean().reset_index(), ax=ax)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This chart shows the average Return on Investment (ROI) for each marketing channel.
*   Highlight which channels are generating the highest returns.
*   Prioritize investment in channels with strong ROI and evaluate the effectiveness of underperforming channels.
""")

# 4. Scatter Plot: Conversion Rate vs. Acquisition Cost
st.subheader("Conversion Rate vs. Acquisition Cost")
fig, ax = plt.subplots()
sns.scatterplot(x='Acquisition_Cost', y='Conversion_Rate', data=df, ax=ax)
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This scatter plot explores the relationship between acquisition cost and conversion rate.
*   Look for trends: do higher acquisition costs lead to higher conversion rates?
*   Identify campaigns that are either high cost with low conversion or low cost with high conversion for further analysis.
""")

# 5. Line Plot: Conversion Rate over Time
st.subheader("Conversion Rate over Time")
# Ensure 'Date' is datetime type for plotting
df['Date'] = pd.to_datetime(df['Date'])
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='Date', y='Conversion_Rate', data=df.sort_values('Date'), ax=ax)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This line plot tracks the conversion rate over time.
*   Observe trends and seasonality in conversion rates.
*   Correlate changes in conversion rate with specific marketing initiatives or external events.
""")

# 6. Bar Chart: Clicks, Impressions, and Engagement Score by Campaign Type
st.subheader("Metrics by Campaign Type")
metrics_df = df.groupby('Campaign_Type')[['Clicks', 'Impressions', 'Engagement_Score']].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
metrics_df.set_index('Campaign_Type').plot(kind='bar', ax=ax)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This chart compares average clicks, impressions, and engagement scores across different campaign types.
*   Understand how different campaign types perform in terms of reach and audience interaction.
*   Use this to optimize campaign strategies based on desired outcomes (e.g., brand awareness vs. direct response).
""")


# 7. Bar Chart: Count of Campaigns by Target Audience
st.subheader("Campaign Count by Target Audience")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(y='Target_Audience', data=df, order=df['Target_Audience'].value_counts().index, ax=ax)
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This chart shows the number of campaigns targeting different audience segments.
*   Identify which audience segments are most frequently targeted.
*   Assess if campaign distribution aligns with strategic priorities or if underserved segments exist.
""")

# 8. Bar Chart: Count of Campaigns by Location
st.subheader("Campaign Count by Location")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(y='Location', data=df, order=df['Location'].value_counts().index, ax=ax)
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This chart shows the distribution of campaigns across different locations.
*   Understand where marketing efforts are concentrated.
*   Evaluate if campaign allocation aligns with market opportunities or requires adjustment.
""")

# 9. Bar Chart: Count of Campaigns by Language
st.subheader("Campaign Count by Language")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(y='Language', data=df, order=df['Language'].value_counts().index, ax=ax)
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This chart shows the number of campaigns conducted in different languages.
*   Identify the primary languages used in campaigns.
*   Consider expanding or adjusting language targeting based on market demographics.
""")

# 10. Bar Chart: Count of Campaigns by Customer Segment
st.subheader("Campaign Count by Customer Segment")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(y='Customer_Segment', data=df, order=df['Customer_Segment'].value_counts().index, ax=ax)
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This chart shows the number of campaigns targeting different customer segments.
*   Understand which customer segments are the focus of marketing efforts.
*   Assess if campaign targeting aligns with business goals and customer value.
""")

# 11. Box Plot: Distribution of ROI by Campaign Type
st.subheader("Distribution of ROI by Campaign Type")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Campaign_Type', y='ROI', data=df, ax=ax)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This box plot visualizes the distribution of ROI for each campaign type.
*   Understand the variability and typical range of ROI within each campaign type.
*   Identify campaign types with consistently high ROI or those with significant outliers.
""")

# 12. Box Plot: Distribution of Acquisition Cost by Channel Used
st.subheader("Distribution of Acquisition Cost by Channel Used")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Channel_Used', y='Acquisition_Cost', data=df, ax=ax)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
plt.close(fig)
st.markdown("""
**Insight:** This box plot shows the distribution of acquisition costs for different marketing channels.
*   Compare the typical cost to acquire a customer across channels.
*   Identify channels with lower acquisition costs for potentially more efficient spending.
""")

st.markdown("""
---
**Overall Insights:**

*   Email and Social Media campaigns show promising average conversion rates, while Google Ads and YouTube have competitive average ROIs, suggesting a balanced channel strategy is key.
*   Acquisition costs vary significantly across channels; optimizing spend on channels with lower costs and higher ROI can improve overall efficiency.
*   Campaign distribution is concentrated in certain target audiences and locations, indicating potential opportunities in underserved segments and regions to expand market reach.
""")
