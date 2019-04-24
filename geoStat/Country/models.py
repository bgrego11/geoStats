from django.db import models

# Create your models here.
class OecdStat(models.Model):
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dwellings_without_basic_facilities_as_pct = models.CharField(db_column='Dwellings without basic facilities as pct', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    housing_expenditure_as_pct = models.IntegerField(db_column='Housing expenditure as pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rooms_per_person_as_rat = models.CharField(db_column='Rooms per person as rat', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    household_net_adjusted_disposable_income_in_usd = models.IntegerField(db_column='Household net adjusted disposable income in usd', blank=True, null=True)  # Field name made lowercase. Field renamedto remove unsuitable characters.
    household_net_financial_wealth_in_usd = models.IntegerField(db_column='Household net financial wealth in usd', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    labour_market_insecurity_as_pct = models.CharField(db_column='Labour market insecurity as pct', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employment_rate_as_pct = models.IntegerField(db_column='Employment rate as pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    long_term_unemployment_rate_as_pct = models.CharField(db_column='Long-term unemployment rate as pct', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personal_earnings_in_usd = models.IntegerField(db_column='Personal earnings in usd', blank=True,null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quality_of_support_network_as_pct = models.IntegerField(db_column='Quality of support network as pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    educational_attainment_as_pct = models.IntegerField(db_column='Educational attainment as pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    student_skills_as_avg_score = models.IntegerField(db_column='Student skills as avg score', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    years_in_education_in_yrs = models.CharField(db_column='Years in education in yrs', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    air_pollution_in_ugm3 = models.IntegerField(db_column='Air pollution in ugm3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    water_quality_as_pct = models.IntegerField(db_column='Water quality as pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stakeholder_engagement_for_developing_regulations_as_avg_score = models.CharField(db_column='Stakeholder engagement for developing regulations as avg score', max_length=255, blank=True, null=True)# Field name made lowercase. Field renamed to remove unsuitable characters.
    voter_turnout_as_pct = models.IntegerField(db_column='Voter turnout as pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    life_expectancy_in_yrs = models.CharField(db_column='Life expectancy in yrs', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    self_reported_health_as_pct = models.IntegerField(db_column='Self-reported health as pct', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oecd_stats'