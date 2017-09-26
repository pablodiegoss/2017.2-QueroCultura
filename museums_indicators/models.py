# from django.db import models
from mongoengine import Document
from mongoengine import MapField
from mongoengine import IntField
from mongoengine import StringField

# -------------------- state indicators --------------------------------


class PercentThematicsMuseumsForState(Document):
    __thematicsMuseumsForState = MapField(required=True)
    __totalMuseumsForState = MapField(required=True)
    _createDate = StringField(required=True)

    @property
    def thmeatics_museums_for_state(self):
        return self._thematicsMuseumsForState

    @thmeatics_museums_for_state.setter
    def thmeatics_museums_for_state(self, number):
        self._thematicsMuseumsForState = number

    @property
    def total_museums_for_state(self):
        return self._totalMuseumsForState

    @total_museums_for_state.setter
    def total_museums_for_state(self, number):
        self._totalMuseumsForState = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


class PercentTypeMuseumsForState(Document):
    __typeMuseumsForState = MapField(required=True)
    __totalMuseumsForState = MapField(required=True)
    _createDate = StringField(required=True)

    @property
    def type_museums_for_state(self):
        return self._typeMuseumsForState

    @type_museums_for_state.setter
    def type_museums_for_state(self, number):
        self._typeMuseumsForState = number

    @property
    def total_museums_for_state(self):
        return self._totalMuseumsForState

    @total_museums_for_state.setter
    def total_museums_for_state(self, number):
        self._totalMuseumsForState = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


class PercentPublicOrPrivateMuseumsForState(Document):
    _totalPublicMuseumsForState = MapField(required=True)
    _totalPrivateMuseumsForState = MapField(required=True)
    _totalMuseumsForState = MapField(required=True)
    _createDate = StringField(required=True)

    @property
    def total_public_museums_for_state(self):
        return self._totalPublicMuseumsForState

    @total_public_museums_for_state.setter
    def total_public_museums_for_state(self, number):
        self._totalPublicMuseumsForState = number

    @property
    def total_private_museums_for_state(self):
        return self._totalPrivateMuseumsForState

    @total_private_museums_for_state.setter
    def total_private_museums_for_state(self, number):
        self._totalPrivateMuseumsForState = number

    @property
    def total_museums_for_state(self):
        return self._totalMuseumsForState

    @total_museums_for_state.setter
    def total_museums_for_state(self, number):
        self._totalMuseumsForState = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


class PercentMuseumsHistoricalArchivePublicAccessForState(Document):
    _totalMuseumsHistoricalArchivePublicAccessForState = \
                                                        MapField(required=True)
    _totalMuseumsForState = MapField(required=True)
    _createDate = StringField(required=True)

    @property
    def total_museums_historical_archive_public_access_for_state(self):
        return self._totalMuseumsHistoricalArchivePublicAccessForState

    @total_museums_historical_archive_public_access_for_state.setter
    def total_museums_historical_archive_public_access_for_state(self, number):
        self._totalMuseumsHistoricalArchivePublicAccessForState = number

    @property
    def total_museums_for_state(self):
        return self._totalMuseumsForState

    @total_museums_for_state.setter
    def total_museums_for_state(self, number):
        self._totalMuseumsForState = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


class PercentMuseumsPromoteGuidedTourForState(Document):
    _totalMuseumsPromoteGuidedTourForState = MapField(required=True)
    _totalMuseumsForState = MapField(required=True)
    _createDate = StringField(required=True)

    @property
    def total_museums_promote_guided_tour_for_state(self):
        return self._totalMuseumsPromoteGuidedTourForState

    @total_museums_promote_guided_tour_for_state.setter
    def totalMuseumsPromoteGuidedTourForState(self, number):
        self._totalMuseumsPromoteGuidedTourForState = number

    @property
    def total_museums_for_state(self):
        return self._totalMuseumsForState

    @total_museums_for_state.setter
    def total_museums_for_state(self, number):
        self._totalMuseumsForState = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


# --------------------- national indicators ----------------------------------
class PercentThematicsMuseums(Document):
    __thematicsMuseums = IntField(required=True)
    __totalMuseums = IntField(required=True)
    _createDate = StringField(required=True)

    @property
    def thmeatics_museums(self):
        return self._thematicsMuseums

    @thmeatics_museums.setter
    def thmeatics_museums(self, number):
        self._thematicsMuseums = number

    @property
    def total_museums(self):
        return self._totalMuseums

    @total_museums.setter
    def total_museums(self, number):
        self._totalMuseums = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


class PercentTypeMuseums(Document):
    __typeMuseums = IntField(required=True)
    __totalMuseums = IntField(required=True)
    _createDate = StringField(required=True)

    @property
    def type_museums(self):
        return self._typeMuseums

    @type_museums.setter
    def type_museums(self, number):
        self._typeMuseums = number

    @property
    def total_museums(self):
        return self._totalMuseums

    @total_museums.setter
    def total_museums(self, number):
        self._totalMuseums = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


class PercentPublicOrPrivateMuseums(Document):
    _totalPublicMuseums = IntField(required=True)
    _totalPrivateMuseums = IntField(required=True)
    _totalMuseums = IntField(required=True)
    _createDate = StringField(required=True)

    @property
    def total_public_museums(self):
        return self._totalPublicMuseums

    @total_public_museums.setter
    def total_public_museums(self, number):
        self._totalPublicMuseums = number

    @property
    def total_private_museums(self):
        return self._totalPrivateMuseums

    @total_private_museums.setter
    def total_private_museums(self, number):
        self._totalPrivateMuseums = number

    @property
    def total_museums(self):
        return self._totalMuseums

    @total_museums.setter
    def total_museums(self, number):
        self._totalMuseums = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


class PercentMuseumsHistoricalArchivePublicAccess(Document):
    _totalMuseumsHistoricalArchivePublicAccess = IntField(required=True)
    _totalMuseums = IntField(required=True)
    _createDate = StringField(required=True)

    @property
    def total_museums_historical_archive_public_access(self):
        return self._totalMuseumsHistoricalArchivePublicAccess

    @total_museums_historical_archive_public_access.setter
    def total_museums_historical_archive_public_access(self, number):
        self._totalMuseumsHistoricalArchivePublicAccess = number

    @property
    def total_museums(self):
        return self._totalMuseums

    @total_museums.setter
    def total_museums(self, number):
        self._totalMuseums = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


class PercentMuseumsPromoteGuidedTour(Document):
    _totalMuseumsPromoteGuidedTour = IntField(required=True)
    _totalMuseums = IntField(required=True)
    _createDate = StringField(required=True)

    @property
    def total_museums_promote_guided_tour(self):
        return self._totalMuseumsPromoteGuidedTour

    @total_museums_promote_guided_tour.setter
    def total_museums_promote_guided_tour(self, number):
        self._totalMuseumsPromoteGuidedTour = number

    @property
    def total_museums(self):
        return self._totalMuseums

    @total_museums.setter
    def total_museums(self, number):
        self._totalMuseums = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


# Amount of Museums registered on year on the platform throughout its existence
class AmountMuseumsRegisteredYear(Document):
    _totalMuseumsRegisteredYear = MapField(required=True)
    _createDate = StringField(required=True)

    @property
    def total_museums_registered_year(self):
        return self._totalMuseumsRegisteredYear

    @total_museums_registered_year.setter
    def total_museums_registered_year(self, number):
        self._totalMuseumsRegisteredYear = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


# Amount of Museums registered monthly on the platform throughout its existence
class AmountMuseumsRegisteredMonth(Document):
    _totalMuseumsRegisteredMonth = MapField(required=True)
    _createDate = StringField(required=True)

    @property
    def total_museums_registered_month(self):
        return self._totalMuseumsRegisteredMonth

    @total_museums_registered_month.setter
    def total_museums_registered_month(self, number):
        self._totalMuseumsRegisteredMonth = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


# Percentage of museums by states
class PercentMuseumsForState(Document):
    _totalMuseumsForState = MapField(required=True)
    _totalMuseums = IntField(required=True)
    _createDate = StringField(required=True)

    @property
    def total_museums_for_state(self):
        return self._totalMuseumsForState

    @total_museums_for_state.setter
    def total_museums_for_state(self, number):
        self._totalMuseumsForState = number

    @property
    def total_museums(self):
        return self._totalMuseums

    @total_museums.setter
    def total_museums(self, number):
        self._totalMuseums = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number
