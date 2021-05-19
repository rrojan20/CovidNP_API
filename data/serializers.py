from rest_framework import serializers

from .models import Daily, Total, DistrictWise


class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily


class DailySerializer(DailySerializer):
    class Meta(DailySerializer.Meta):
        fields = (
            "new_cases",
            "male_cases_estimated",
            "female_cases_estimated",
            "recovered",
            "deaths",
            "date_updated",
        )


class DailyMaleSerializer(DailySerializer):
    class Meta(DailySerializer.Meta):
        fields = ("male_cases_estimated", "date_updated")


class DailyFemaleSerializer(DailySerializer):
    class Meta(DailySerializer.Meta):
        fields = ("female_cases_estimated", "date_updated")


class TotalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total


class TotalSerializer(TotalBaseSerializer):
    class Meta(TotalBaseSerializer.Meta):
        fields = (
            "total_cases",
            "total_infected",
            "total_male_estimated",
            "total_female_estimated",
            "recovered",
            "deaths",
            "date_updated",
        )


class TotalMaleSerializer(TotalBaseSerializer):
    class Meta(TotalBaseSerializer.Meta):
        fields = (
            "total_male_estimated",
            "date_updated",
        )


class TotalFemaleSerializer(TotalBaseSerializer):
    class Meta(TotalBaseSerializer.Meta):
        fields = (
            "total_female_estimated",
            "date_updated",
        )


class DistrictWiseBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictWise

class DistrictWiseSerializer(DistrictWiseBaseSerializer):
    class Meta(DistrictWiseBaseSerializer.Meta):
        fields = (
            "district",
            "total_cases",
            "total_male",
            "total_female",
            "daily_cases_estimated",
            "daily_male_estimated",
            "daily_female_estimated",
            "date_updated",
        )

class DistrictWiseMaleSerializer(DistrictWiseBaseSerializer):
    class Meta(DistrictWiseBaseSerializer.Meta):
        fields = (
            "total_male",
            "daily_male_estimated",
        )

class DistrictWiseFemaleSerializer(DistrictWiseBaseSerializer):
    class Meta(DistrictWiseBaseSerializer.Meta):
        fields = (
            "total_female",
            "daily_female_estimated",
        )